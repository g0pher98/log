setImmediate(function() {
    Java.perform(function() {
        var chall_07 = Java.use("uk.rossmarks.fridalab.challenge_07");
        Java.choose("uk.rossmarks.fridalab.MainActivity", {
            onMatch: function(instance) {
                for (var i = 1000; i < 10000; i ++) {
                    if (chall_07.check07Pin(String(i))) {
                        instance.chall07(String(i))
                    }
                }
            },
            onComplete: function() {}
        });
        
    }) 
})