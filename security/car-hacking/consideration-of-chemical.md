# Consideration of DBC
DBC 파일을 분석하고, 어떤식으로 공격해야 효율적일지 고찰한 결과를 작성해보려고 한다. 분석은 cantools repo에 있던 example 중 가장 차량 ECU와 관련된 것처럼 생긴 abs.dbc를 분석해보려고 한다. 나름대로 분리해본  step별로 진행된다.  

분석 중 알게된 내용인데, 해당 DBC 파일은 Bosch Motorsport라는 Bosch의 자동차 기술 관련 자회사에서 개발한 ABS M5 Kit에 대한 내용임을 알 수 있었다. ABS M5 kit 구조는 [이 문서](https://www.bosch-motorsport.com/content/downloads/Raceparts/Resources/pdf/Operation%20Manual_70618763_ABS_M5_Kit.pdf)를 통해 확인할 수 있다.  



## Step 1. 기본정보
```xml
VERSION ""

...

CM_ "Version 2.0";
```
여전히 어떤 버전을 말하는건지 모르겠지만(아마 dbc 포맷 버전일듯?) 값은 비어있다. 구조분석에 큰 영향을 주는 요인은 아니니 일단 패스.

```xml
NS_ : 
	NS_DESC_
    ...
	SG_MUL_VAL_
```
각종 심볼들이 정의되어있는데, 아직도 이 `NS_`가 정확히 어떤 역할을 하는지는 파악하지 못했다.

```xml
BS_:
```
baudrate는 기본값으로 설정된다.

```xml
BU_: ABS DRS_MM5_10
```
node는 `ABS`, `DRS_MM5_10` 이렇게 두 개가 있음을 알 수 있다.

```xml
VAL_TABLE_ ABS_fault_info 2 "active faults stored" 1 "inactive faults stored" 0 "no faults stored" ;
VAL_TABLE_ vt_WheelSpeedQualifier 5 "InvalidUnderVoltage" 4 "NotCalculated" 3 "ReducedMonitored" 2 "Faulty" 1 "Normal" 0 "NotInitialized" ;
```
`VAL_TABLE_`은 처음나온 심볼인데, 저번에 처음 분석할 때 나왔던 `VAL`과 매우 비슷한 역할을 한다. 조금 더 조사해보니 실제로 지난번에 분석했던 `VAL_` 사용 방법이 사실 `VAL_TABLE_`의 사용 방법이고, `VAL_`에는 `VAL_TABLE_`에서 정의한 TABLE NAME을 기입하여 사용하는 것이라고 한다. `VAL_TABLE_` 구조는 다음과 같다.
```
VAL_TABLE_ <ValueTableName> <ValueTableDefinition> <...>;
```
여기에 `<...>` 부분에는 다음과 같은 내용이 공백을 기준으로 반복된다.
```
<IntValue> <"StringValue">
```
지난 분석 때 보았던 `VAL_` 구조와 매우 똑같다. 정확하게는 지난번 조사가 잘못된 것이고 실제 `VAL_` 구조는 다음과 같다.
```
VAL_ <CAN-ID> <SignalsName> <ValTableName|ValTableDefinition>;
```
구조에서 볼 수 있듯 앞서 정의한 `VAL_TABLE_`의 명칭으로 signal 값 의미를 기술할 수 있다. 구조는 이렇지만 사실 저번 분석때 보았던 dbc는 `VAL_`을 `VAL_TABLE_`처럼 사용했으니, `VAL_`은 구조가 비교적 자유롭다(?)로 볼 수 있을 것 같다. `VAL_`이 `VAL_TABLE_`을 포함하는 구조라고 보는게 가장 적절해보인다.

## Step 2. Message 구조분석
이제부터는 주석들을 잘 활용하여 메세지를 분석해보자.
```xml
BO_ 835 BREMSE_33: 8 ABS
 SG_ whlspeed_FL : 0|16@1+ (0.015625,0) [0|100] "m/s" Vector__XXX
 SG_ whlspeed_FR : 16|16@1+ (0.015625,0) [0|100] "m/s" Vector__XXX
 SG_ whlspeed_RL : 32|16@1+ (0.015625,0) [0|100] "m/s" Vector__XXX
 SG_ whlspeed_RR : 48|16@1+ (0.015625,0) [0|100] "m/s" Vector__XXX
```
835번 Message는 `ABS` 노드가 전송하는 `BREMSE_33` 이라는 `8bytes` 메세지로, 다음과 같은 시그널을 포함하는 구조를 가지고 있다.
- whlspeed_FL : 0bit 위치부터 시작하는 총 16bit의 데이터이며, unsigned 리틀엔디안 데이터다. `Vector__XXX`가(?) 수신한다.
- whlspeed_FR : 16bit 위치부터 시작하는 총 16bit의 데이터이며, 성격은 앞의 시그널과 같다.
- whlspeed_RL : 16bit 위치부터 시작하는 총 16bit의 데이터이며, 성격은 앞의 시그널과 같다.
- whlspeed_RR : 16bit 위치부터 시작하는 총 16bit의 데이터이며, 성격은 앞의 시그널과 같다.

835번에 대한 `CM` 데이터도 존재하는데, 다음과 같다.
```
CM_ SG_ 835 whlspeed_FL "Radgeschwindigkeit / wheel speed absCtrl FL";
CM_ SG_ 835 whlspeed_FR "Radgeschwindigkeit / wheel speed absCtrl FR";
CM_ SG_ 835 whlspeed_RL "Radgeschwindigkeit / wheel speed absCtrl RL";
CM_ SG_ 835 whlspeed_RR "Radgeschwindigkeit / wheel speed absCtrl RR";
```
`Radgeschwindigkeit`는 독일어로 휠 속도를 말한다. absCtrl은 정확하진 않지만 브레이크 조절을 담당하는 ABS(Anti-lock Braking System) 인 것으로 보인다. ABS는 자동차의 안정적인 제동을 위해 브레이크를 연속적으로 제어하지 않고, 걸었다 풀었다가를 반복하도록 하는데, ECU에서 유압제어장치를 통해 제어한다고 한다. 각 바퀴별로 하나씩 시그널이 존재하며, 주석이 깔끔한 설명은 아니라(~~내가 무면허라 그런가?~~) 정확히 어떤 동작을 수행하는지는 모르겠지만, 크게 바퀴 속도를 제어하는 역할을 하는 것으로 보인다.

```
BO_ 320 BREMSE_10: 8 ABS

BO_ 321 BREMSE_11: 8 ABS

BO_ 322 BREMSE_12: 8 ABS

BO_ 323 BREMSE_13: 8 ABS

BO_ 117 DRS_RX_ID0: 8 ABS
```
세부적인 주석도 따로 없는 메세지들이다. 메세지 자체가 하나의 의미를 가지는 것으로 보인다.
- BREMSE_10 ~ 13 : 순서대로 320 ~ 323번을 부여받으며, ABS가 송신하는 8bytes의 메세지다.
    - 독일어로 BREMSE는 브레이크를 말한다. 브레이크를 제어하는 신호로 추측된다.
- DRS_RX_ID0 : 117 부여받으며, ABS가 송신하는 8bytes의 메세지다.
    - 차량에서 DRS(Drag Reduction System)은 흔히 레이싱카의 뒷날개라고 부르는(~~나만그랬나??~~) 부분을 말하며, 추격 대상의 차량이 매우 가까운 거리에 있을 때, 순간적으로 항력을 줄여 최고속도를 높임으로써 추월이 가능하도록 돕는 장치를 말한다.
    - RX의 경우 보통 데이터 신호가 들어오는 부분을 말한다.
    - 위 정보를 종합했을 때, DRS 조정을 담당하는 시그널로 추정된다.

```xml
BO_ 112 MM5_10_TX1: 8 DRS_MM5_10
 SG_ Yaw_Rate : 0|16@1+ (0.005,-163.84) [-163.84|163.83] "�/s"  ABS
 SG_ AY1 : 32|16@1+ (0.000127465,-4.1768) [-4.1768|4.1765] "g"  ABS

BO_ 128 MM5_10_TX2: 8 DRS_MM5_10
 SG_ Roll_Rate : 0|16@1+ (0.005,-163.84) [-163.84|163.835] "�/s"  ABS
 SG_ AX1 : 32|16@1+ (0.000127465,-4.1768) [-4.1768|4.1765] "g"  ABS

BO_ 1398 MM5_10_TX3: 8 DRS_MM5_10
 SG_ AZ : 32|16@1+ (0.000127465,-4.1768) [-4.1768|4.1765] "g"  ABS

...

CM_ SG_ 112 Yaw_Rate "Measured yaw rate around the Z axle.";
CM_ SG_ 112 AY1 "Measured lateral acceleration.";
CM_ SG_ 128 Roll_Rate "Measured roll rate around the X axle.";
CM_ SG_ 128 AX1 "Measured longitudional acceleration.";
CM_ SG_ 1398 AZ "Measured vertical acceleration.";
```
`MM5`라는 키워드에 빠져 삽질을 엄청 했는데, 아래 확인해보니 시그널에 대해 주석이 있었다.  
각 시그널은 다음과 같다.
- Yaw_Rate : Yaw 측정값
- AY1 : 횡방향 가속도
- Roll_Ratet : Roll 측정값
- AX1 : 종방향 가속도
- AZ : 수직 가속도
위 시그널을 기반으로 `MM5` 키워드를 사용하는 메세지는 차량의 회전상태와 관련된 메세지임을 추측할 수 있다.

```xml
BO_ 586 BREMSE_2: 8 ABS
 SG_ whlspeed_FL_Bremse2 : 0|16@1+ (0.015625,0) [0|100] "m/s" Vector__XXX
 SG_ whlspeed_FR_Bremse2 : 16|16@1+ (0.015625,0) [0|100] "m/s" Vector__XXX
 SG_ whlspeed_RL_Bremse2 : 32|16@1+ (0.015625,0) [0|100] "m/s" Vector__XXX
 SG_ whlspeed_RR_Bremse2 : 48|16@1+ (0.015625,0) [0|100] "m/s" Vector__XXX

...

CM_ SG_ 586 whlspeed_FL_Bremse2 "Radgeschwindigkeit / wheel speed direct FL";
CM_ SG_ 586 whlspeed_FR_Bremse2 "Radgeschwindigkeit / wheel speed direct FR";
CM_ SG_ 586 whlspeed_RL_Bremse2 "Radgeschwindigkeit / wheel speed direct RL";
CM_ SG_ 586 whlspeed_RR_Bremse2 "Radgeschwindigkeit / wheel speed direct RR";
```
앞서 분석한 `BREMSE_33` 메세지와 마찬가지로 본 메세지는 휠 브레이크를 제어하는 메세지로 볼 수 있다.

```xml
BO_ 588 ABS_Switch: 8 Vector__XXX
 SG_ ABS_Switchposition : 0|8@1+ (1,0) [0|11] ""  ABS

...

CM_ SG_ 588 ABS_Switchposition "Channel to send the swich position via CAN to the ABS.";
```
`ABS_Switch` 메세지는 특정 Veector가 ABS로 송신하는 8bytes의 메세지다. 주석에 의하면 CAN 통신을 사용해서 ABS로 swich position 데이터를 송신하는 채널이라고 설명되어있다.

```xml
BO_ 832 BREMSE_30: 8 ABS

BO_ 833 BREMSE_31: 8 ABS
 SG_ Idle_Time : 16|16@1+ (1,0) [0|0] "-" Vector__XXX
```
마찬가지로 브레이크 관련 메세지다.

```
BO_ 834 BREMSE_32: 8 ABS
 SG_ acc_FA : 0|8@1+ (0.05,0) [0|10] "cm3" Vector__XXX
 SG_ acc_RA : 8|8@1+ (0.05,0) [0|10] "cm3" Vector__XXX
 SG_ WheelQuality_FL : 32|8@1+ (1,0) [0|32] "" Vector__XXX
 SG_ WheelQuality_FR : 40|8@1+ (1,0) [0|32] "" Vector__XXX
 SG_ WheelQuality_RL : 48|8@1+ (1,0) [0|32] "" Vector__XXX
 SG_ WheelQuality_RR : 56|8@1+ (1,0) [0|32] "" Vector__XXX

...

CM_ SG_ 834 acc_FA "Fill level of the fluid reservoir of the front axle.";
CM_ SG_ 834 acc_RA "Fill level of the fluid reservoir of the rear axle.";

CM_ SG_ 834 WheelQuality_FL "Bit matrix
Bit0 ( 1) Signal Reduced Monitored
Bit1 ( 2) Reduced Accuracy
Bit2 ( 4) Interfered
Bit3 ( 8) Suspicious Plausibility
Bit4 (16) Suspicious Lost
Bit5 (32) Not Initialized
Bit6 (64) Invalid Generic
Bit7 (128) Invalid Individual";

CM_ SG_ 834 WheelQuality_FR "Bit matrix
Bit0 ( 1) Signal Reduced Monitored
Bit1 ( 2) Reduced Accuracy
Bit2 ( 4) Interfered
Bit3 ( 8) Suspicious Plausibility
Bit4 (16) Suspicious Lost
Bit5 (32) Not Initialized
Bit6 (64) Invalid Generic
Bit7 (128) Invalid Individual";

CM_ SG_ 834 WheelQuality_RL "Bit matrix
Bit0 ( 1) Signal Reduced Monitored
Bit1 ( 2) Reduced Accuracy
Bit2 ( 4) Interfered
Bit3 ( 8) Suspicious Plausibility
Bit4 (16) Suspicious Lost
Bit5 (32) Not Initialized
Bit6 (64) Invalid Generic
Bit7 (128) Invalid Individual";

CM_ SG_ 834 WheelQuality_RR "Bit matrix
Bit0 ( 1) Signal Reduced Monitored
Bit1 ( 2) Reduced Accuracy
Bit2 ( 4) Interfered
Bit3 ( 8) Suspicious Plausibility
Bit4 (16) Suspicious Lost
Bit5 (32) Not Initialized
Bit6 (64) Invalid Generic
Bit7 (128) Invalid Individual";
```
`BREMSE_32` 메세지는 차축 및 휠 신뢰도에 대한 정보를 포함한다.
- acc_FA : 전방 차축
- acc_RA : 후방 차축
- WheelQuality_XX : 휠 데이터 성격
    - 신호 세기, 손실, 신뢰도 등 휠 데이터에 대한 정보들이 있는 것을 확인할 수 있다.

```
BO_ 1345 BREMSE_51: 8 ABS
 SG_ AX1_ABS_int : 0|16@1+ (0.00012742,-4.1768) [-4.1768|4.1736697] "g" Vector__XXX
 SG_ AY1_ABS_int : 16|16@1+ (0.00012742,-4.1768) [-4.1768|4.1765] "g" Vector__XXX
 SG_ IF_variant : 48|6@1+ (1,0) [0|63] "" Vector__XXX
 SG_ IF_revision : 54|6@1+ (1,0) [0|63] "" Vector__XXX
 SG_ IF_chksum : 60|4@1+ (1,0) [0|15] "" Vector__XXX

...

CM_ SG_ 1345 AX1_ABS_int "Used longitudional acceleration value in the ABS.";
CM_ SG_ 1345 AY1_ABS_int "Used lateral acceleration value in the ABS.";
CM_ SG_ 1345 IF_variant "external info to e.g. MS6 which dbc has to be used. This index increments on changes that make the MS6 interface incompatible to the predecessor CAN interface implementation";
CM_ SG_ 1345 IF_revision "external info to e.g. MS6 which dbc has to be used. This index increments with added features (rest of MS6 interface stays intact.)";
CM_ SG_ 1345 IF_chksum "external info to e.g. MS6 which dbc has to be used. Checksum ";
```
`BREMSE_51` 메세지는 주로 확장 기능에 대한 메세지로 보인다.
- `AX1_ABS_int`: ABS에서 사용하는 X축 가속도 값.
- `AY1_ABS_int`: ABS에서 사용하는 Y축 가속도 값.
- `IF_*` : 확장 데이터에 대한 정보. MS6이라는 압력 레귤레이터(?) DBC를 사용해야 한다고 한다.

```xml
BO_ 1346 BREMSE_52: 8 ABS
 SG_ Mplx_SW_Info M : 0|8@1+ (1,0) [0|255] "" Vector__XXX
 SG_ SW_version_High_upper m1 : 8|8@1+ (1,0) [0|255] "" Vector__XXX
 SG_ SW_version_High_lower m1 : 16|8@1+ (1,0) [0|255] "" Vector__XXX
 SG_ SW_version_Mid_upper m1 : 24|8@1+ (1,0) [0|255] "" Vector__XXX
 SG_ SW_version_Mid_lower m1 : 32|8@1+ (1,0) [0|255] "" Vector__XXX
 SG_ SW_version_Low_upper m1 : 40|8@1+ (1,0) [0|255] "" Vector__XXX
 SG_ SW_version_Low_lower m1 : 48|8@1+ (1,0) [0|255] "" Vector__XXX
 SG_ BB_dig1 m2 : 8|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ BB_dig2 m2 : 16|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ BB_dig3 m2 : 24|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ BB_dig4 m2 : 32|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ BB_dig5 m2 : 40|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ BB_dig6 m2 : 48|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ BB_dig7 m2 : 56|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_01 m3 : 8|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_02 m3 : 16|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_03 m3 : 24|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_04 m3 : 32|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_05 m3 : 40|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_06 m3 : 48|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_07 m3 : 56|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_08 m4 : 8|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_09 m4 : 16|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_10 m4 : 24|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_11 m4 : 32|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_12 m4 : 40|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_13 m4 : 48|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_Id_14 m4 : 56|8@1+ (1,0) [0|255] "ASCII" Vector__XXX
 SG_ Appl_date_01 m5 : 8|8@1+ (1,0) [0|99] "" Vector__XXX
 SG_ Appl_date_02 m5 : 16|8@1+ (1,0) [1|12] "" Vector__XXX
 SG_ Appl_date_03 m5 : 24|8@1+ (1,0) [1|31] "" Vector__XXX
 SG_ Appl_date_04 m5 : 32|8@1+ (1,0) [0|24] "" Vector__XXX
 SG_ Appl_date_05 m5 : 40|8@1+ (1,0) [0|59] "" Vector__XXX
 SG_ Appl_date_06 m5 : 48|8@1+ (1,0) [0|59] "" Vector__XXX
 SG_ SW_CAN_ident m6 : 8|8@1+ (1,0) [0|255] "" Vector__XXX
 SG_ HU_date_year m7 : 8|8@1+ (1,0) [0|99] "" Vector__XXX
 SG_ HU_date_month m7 : 16|8@1+ (1,0) [1|12] "" Vector__XXX
 SG_ HU_date_day m7 : 24|8@1+ (1,0) [1|31] "" Vector__XXX
 SG_ Ecu_serial m7 : 32|32@1+ (1,0) [0|99999] "" Vector__XXX

 ...

CM_ SG_ 1346 Mplx_SW_Info "1=SW version; 2=BB#; 3,4=application name; 5=application date (UTC); 6=deviceType (SW CAN ident, ABS M5=2, ABS M6=3); 7=Serial#";
CM_ SG_ 1346 SW_version_High_upper "version 1.0 as 0x01(upper), version 100.20 as 0x64(upper)";
CM_ SG_ 1346 SW_version_High_lower "version 1.0 as 0x00(lower), version 100.20 as 0x14(lower)";
CM_ SG_ 1346 SW_version_Mid_upper "version 1.0 as 0x01(upper), version 100.20 as 0x64(upper)";
CM_ SG_ 1346 SW_version_Mid_lower "version 1.0 as 0x00(lower), version 100.20 as 0x14(lower)";
CM_ SG_ 1346 SW_version_Low_upper "version 1.0 as 0x01(upper), version 100.20 as 0x64(upper)";
CM_ SG_ 1346 SW_version_Low_lower "version 1.0 as 0x00(lower), version 100.20 as 0x14(lower)";
CM_ SG_ 1346 Appl_date_01 "year";
CM_ SG_ 1346 Appl_date_02 "month";
CM_ SG_ 1346 Appl_date_03 "day";
CM_ SG_ 1346 Appl_date_04 "hour";
CM_ SG_ 1346 Appl_date_05 "minute";
CM_ SG_ 1346 Appl_date_06 "seconds";
```
`BREMSE_52` 메세지는 소프트웨어에 대한 메타데이터를 기술하는 메세지로, 내용이 좀 자세하다. 가장 먼저 오는 `Mplx_SW_Info` 시그널에 따라 본 메세지가 내포하고 있는 데이터의 성격이 달라진다.
- `Mplx_SW_Info` : 데이터의 성격을 표기
    - 1 : 소프트웨어 버전정보
    - 2 : BB (? 뭐지)
    - 3 : 어플리케이션 명칭
- `SW_version_*_uppder/lower` : 버전 정보 표기
    - 크게 High, Mid, Low 세 부분으로 나뉘며, 각 부분별로 upper와 lower 버전이 존재한다.
- `BB_dig1 ~ 7` : 모르겠음.
- `Appl_Id_01 ~ 14` : 모르겠음.
- `Appl_date_01 ~ 06` : 순서대로 `연/월/일/시/분/초` 를 뜻한다.  

`BB_dig`와 `Appl_Id_` 시그널은 코멘트도 없고, M5 공식문서에도 없다. 검색해도 안나와서 자세한 정보를 아직 알 수 없다. 

```xml
BO_ 1376 BREMSE_50: 8 ABS
 SG_ Brake_bal_at50 : 16|16@1+ (0.1,0) [0|100] "Bar" Vector__XXX
 SG_ Brake_bal_at50_advice : 32|8@1+ (1,0) [0|100] "Bar" Vector__XXX
 SG_ Brake_bal_pct : 40|16@1+ (0.1,0) [0|100] "%" Vector__XXX
 SG_ Brake_bal_pct_advice : 56|8@1+ (1,0) [0|100] "%" Vector__XXX

...

CM_ SG_ 1376 Brake_bal_at50 "Calculated rear axle brake pressure if the front pressure is at 50 bar.";
CM_ SG_ 1376 Brake_bal_at50_advice "Recommended rear axle brake pressure if the front pressure is at 50 bar.";
CM_ SG_ 1376 Brake_bal_pct "Percental brake balance on the front axle. ";
CM_ SG_ 1376 Brake_bal_pct_advice "Recommended percental brake balance on the front axle. ";
```
`BREMSE_50` 메세지는 브레이크의 압력 및 밸런스 데이터를 다룬다.
- `Brake_bal_at50` : 전면 압력이 50bar일 경우, 후방차축 브레이크 압력 계산값.
- `Brake_bal_at50_advice` : 전면 압력이 50bar일 경우, 후방차축 브레이크 압력 권장값.
- `Brake_bal_pct` : 전방차축의 브레이크 밸런스(백분율).
- `Brake_bal_pct_advice` : 전방차축의 권장 브레이크 밸런스(백분율).


```xml
BO_ 1472 BREMSE_53: 8 ABS
 SG_ SwitchPosition : 0|8@1+ (1,0) [1|12] "" Vector__XXX
 SG_ P_FA : 8|16@1- (0.01526,0) [-42.5|425] "bar" Vector__XXX
 SG_ BLS : 24|1@1+ (1,0) [0|1] "" Vector__XXX
 SG_ Bremse_53_cnt : 26|2@1+ (1,0) [0|3] "" Vector__XXX
 SG_ ABS_Malfunction : 28|1@1+ (1,0) [0|1] "" Vector__XXX
 SG_ ABS_Active : 29|1@1+ (1,0) [0|1] "" Vector__XXX
 SG_ EBD_Lamp : 30|1@1+ (1,0) [0|1] "" Vector__XXX
 SG_ ABS_Lamp : 31|1@1+ (1,0) [0|1] "" Vector__XXX
 SG_ Diag_FL : 32|2@1+ (1,0) [0|3] "" Vector__XXX
 SG_ Diag_FR : 34|2@1+ (1,0) [0|3] "" Vector__XXX
 SG_ Diag_RL : 36|2@1+ (1,0) [0|3] "" Vector__XXX
 SG_ Diag_RR : 38|2@1+ (1,0) [0|3] "" Vector__XXX
 SG_ Diag_ABSUnit : 40|1@1+ (1,0) [0|1] "" Vector__XXX
 SG_ Diag_FuseValve : 41|1@1+ (1,0) [0|1] "" Vector__XXX
 SG_ Diag_FusePump : 42|1@1+ (1,0) [0|1] "" Vector__XXX
 SG_ Diag_P_FA : 43|1@1+ (1,0) [0|1] "" Vector__XXX
 SG_ Diag_P_RA : 44|1@1+ (1,0) [0|1] "" Vector__XXX
 SG_ Diag_YRS : 45|1@1+ (1,0) [0|1] "" Vector__XXX
 SG_ ABS_fault_info : 46|2@1+ (1,0) [0|3] "" Vector__XXX
 SG_ P_RA : 48|16@1- (0.01526,0) [-42.5|425] "bar" Vector__XXX

...

CM_ SG_ 1472 SwitchPosition "Used switch position of the ABS.";
CM_ SG_ 1472 P_FA "Brake pressure on the front axle.";
CM_ SG_ 1472 BLS "Bit for the brake light switch.";
CM_ SG_ 1472 ABS_Malfunction "Bit will jump to 1, if the ABS control is deactivated by a fault.";
CM_ SG_ 1472 ABS_Active "Bit will jump to 1, when the ABS control is active.";
CM_ SG_ 1472 EBD_Lamp "Bit will jump to 1, when the EBD is deactivated due to a fault.";
CM_ SG_ 1472 ABS_Lamp "Bit will jump to 1, when the ABS control is deactivated due to a fault, switch to the off position or while working with RaceABS.";
CM_ SG_ 1472 Diag_FL "Value to show faults related to the wheel speed sensor. 
0 - Signal ok, 1 - Wiring related fault, 2 - Signal related fault";
CM_ SG_ 1472 Diag_FR "Value to show faults related to the wheel speed sensor. 
0 - Signal ok, 1 - Wiring related fault, 2 - Signal related fault";
CM_ SG_ 1472 Diag_RL "Value to show faults related to the wheel speed sensor. 
0 - Signal ok, 1 - Wiring related fault, 2 - Signal related fault";
CM_ SG_ 1472 Diag_RR "Value to show faults related to the wheel speed sensor. 
0 - Signal ok, 1 - Wiring related fault, 2 - Signal related fault";
CM_ SG_ 1472 Diag_ABSUnit "Bit to show, if a ABS error related to the hydraulic unit is present";
CM_ SG_ 1472 Diag_FuseValve "Bit to show, if a ABS error related to the fuse or power supply of the ABS valves is present.";
CM_ SG_ 1472 Diag_FusePump "Bit to show, if a ABS error related to the fuse or power supply of the ABS pump is present.";
CM_ SG_ 1472 Diag_P_FA "Bit to show, if the pressure sensor FA is working properly. An error is pressent, if the bit is 1.";
CM_ SG_ 1472 Diag_P_RA "Bit to show, if the pressure sensor RA is working properly. An error is pressent, if the bit is 1.";
CM_ SG_ 1472 Diag_YRS "Bit to show, if the yaw rate sensor is working properly. An error is pressent, if the bit is 1.";
CM_ SG_ 1472 ABS_fault_info "Bit matrix to show if a fault or a active fault is stored in the ABS. Bit will also show minor errors which do  not shut down the ABS controller.";
CM_ SG_ 1472 P_RA "Brake pressure on the rear axle.";

...

VAL_ 1472 Diag_FL 2 "Signal error" 1 "Line error" 0 "Signal ok" ;
VAL_ 1472 Diag_FR 2 "Signal error" 1 "Line error" 0 "Signal ok" ;
VAL_ 1472 Diag_RL 2 "Signal error" 1 "Line error" 0 "Signal ok" ;
VAL_ 1472 Diag_RR 2 "Signal error" 1 "Line error" 0 "Signal ok" ;
VAL_ 1472 ABS_fault_info 2 "active faults stored" 1 "inactive faults stored" 0 "no faults stored" ;
```
`BREMSE_53` 메세지는 기기의 결함을 체크하는 용도로 보인다.
- `SwitchPosition`: ABS에서 사용하는 position 정보
- `P_FA` : 전방차축 브레이크 압력
- `BLS` : 브레이크 조명 스위치
- `Bremse_53_cnt` : 모르겠음.
- `ABS_Malfunction` : ABS 고장으로 인한 비활성화 여부
- `ABS_Active` : ABS 활성화 여부
- `EBD_Lamp` : 결함이 발생해서 EBD가 비활성화되는 경우
- `ABS_Lamp` : 결함이 발생해서 ABS가 비활성화되는 경우
- `Diag_XX` : 휠 속도 센서와 관련된 고장 여부
    - 0 : OK
    - 1 : 배선 고장
    - 2 : 신호 고장
- `Diag_ABSUnit` : 수압 장치와 관련된 ABS 오류
- `Diag_FuseValve` : ABS 밸브의 퓨즈 또는 전원 공급과 관련된 오류
- `Diag_FusePump` : ABS 펌프의 퓨즈 또는 전원 공급과 관련된 오류
- `Diag_P_FA` : 전방차축 압력센서 정상작동 여부
- `Diag_P_RA` : 후방차축 압력센서 정상작동 여부
- `Diag_YRS` : Yaw rate sensor 정상작동 여부
- `ABS_fault_info` : 결함 정보가 ABS에 저장되어있는지 여부
- `P_RA` : 후방차축 브레이크 압력

## Step 3. 추가 속성 값
`BA_DEF_` 심볼은 속성을 선언하는 심볼이다. 다음 포맷으로 속성의 자료형을 선언할 수 있다.
```
BA_DEF_ [BU_|BO_|SG_] "<AttributeName>" <DataType> [Config];
```
`BA_DEF_DEF_` 심볼은 `BA_DEF_`로 선언된 속성에 default 값을 지정해줄 수 있다. 다음 포맷으로 속성의 기본값을 설정할 수 있다.
```
BA_DEF_DEF_ "<AttributeName>" ["]<DefaultValue>["];
```


본 dbc에서는 다음과 같이 속성들이 정의되었다.
```xml
BA_DEF_ BO_  "GenMsgCycleTime" INT 1 3000;
BA_DEF_ BO_  "VFrameFormat" ENUM  "StandardCAN","ExtendedCAN","reserved","reserved","reserved","reserved","reserved","reserved","reserved","reserved","reserved","reserved","reserved","reserved","StandardCAN_FD","ExtendedCAN_FD";
BA_DEF_  "BusType" STRING ;
BA_DEF_DEF_  "GenMsgCycleTime" 10;
BA_DEF_DEF_  "VFrameFormat" "";
BA_DEF_DEF_  "BusType" "CAN";
```

`BA_` 심볼은 속성값을 값과 함께 정의할 수 있다. 위 두 심볼을 모두 포함한다고 생각해도 된다. 포맷은 다음과 같다.
```
BA_ "<AttributeName>" [BU_|BO_|SG_] [Node|CAN-ID] [SignalName] <AttributeValue>;
```
본 dbc에서는 다음과 같이 주요 속성에 대한 값을 정의했다.

```xml
BA_ "BusType" "CAN";
BA_ "VFrameFormat" BO_ 835 0;
BA_ "VFrameFormat" BO_ 320 0;
BA_ "VFrameFormat" BO_ 321 0;
BA_ "VFrameFormat" BO_ 322 0;
BA_ "VFrameFormat" BO_ 323 0;
BA_ "VFrameFormat" BO_ 117 0;
BA_ "VFrameFormat" BO_ 112 0;
BA_ "VFrameFormat" BO_ 128 0;
BA_ "VFrameFormat" BO_ 1398 0;
BA_ "VFrameFormat" BO_ 586 0;
BA_ "VFrameFormat" BO_ 588 0;
BA_ "VFrameFormat" BO_ 832 0;
BA_ "VFrameFormat" BO_ 833 0;
BA_ "VFrameFormat" BO_ 834 0;
BA_ "VFrameFormat" BO_ 1345 0;
BA_ "VFrameFormat" BO_ 1346 0;
BA_ "VFrameFormat" BO_ 1376 0;
BA_ "VFrameFormat" BO_ 1472 0;
```
BusType 변수에 CAN 통신임을 정의하고, VFrameFormat 데이터를 모두 0으로 설정한 것을 확인할 수 있다.


## Reference
- DBC Symbols : https://github.com/stefanhoelzl/CANpy/blob/master/docs/DBC_Specification.md
- ABS : https://ko.wikipedia.org/wiki/ABS
- DRS : https://ko.wikipedia.org/wiki/%EB%93%9C%EB%9E%98%EA%B7%B8_%EB%A6%AC%EB%8D%95%EC%85%98_%EC%8B%9C%EC%8A%A4%ED%85%9C