from bitcoin.rpc import RawProxy

class Balance:
    def __init__(self, api, address, start_block_height=0, debug=False):
        self.api = api
        self.debug = debug
        self.address = address
        
        self.utxo = {}

        self.total_height = api.getblockcount()
        self.start_block_height = start_block_height
        self.next_block_hash = api.getblockhash(start_block_height)
    
    def calc(self):
        while True:
            block = api.getblock(self.next_block_hash, 2)

            for tx in block['tx']:
                self.check_vin(tx)
                self.check_vout(tx)

            if self.is_lastblock(block):
                break
        
        return sum([float(self.utxo[txid]['value']) for txid in self.utxo.keys()])
                
    
    def check_vin(self, tx):
        for vin in tx['vin']:
            if 'txid' in vin and (vin['txid'] in self.utxo) and (vin['vout'] == self.utxo[vin['txid']]['index']):
                if self.debug:
                    print(f"[vin] {vin['txid']}[{vin['vout']}] {self.utxo[vin['txid']]['value']}")
                del self.utxo[vin['txid']]

    def check_vout(self, tx):
        for idx, vout in enumerate(tx['vout']):
            if "address" in vout['scriptPubKey']:
                out_address = vout['scriptPubKey']['address']
                if(self.address == out_address):
                    if self.debug:
                        print(f"[vout] {tx['txid']}[{idx}] {vout['value']}")
                    self.utxo[tx['txid']] = {
                        "value": vout['value'],
                        "index": idx
                    }

    
    def is_lastblock(self, block):
        if self.debug and self.start_block_height % 5000 == 0:
            print(f"[*] {self.start_block_height} / {self.total_height}")

        if 'nextblockhash' in block:
            self.next_block_hash = block['nextblockhash']
            self.start_block_height += 1
            return False

        return True


if __name__ == "__main__":
    api = RawProxy(service_port=18332)
    alice_address = "mp5eDBnzVsKWBX5T1qNBmkuDiPwFxdYBxk" # testnet

    balance = Balance(api, alice_address, start_block_height=2090000, debug=True)
    print(balance.calc())


