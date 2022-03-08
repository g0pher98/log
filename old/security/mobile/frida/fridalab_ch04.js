setImmediate(function() {
    Java.perform(function() {
        Java.choose("uk.rossmarks.fridalab.MainActivity", {
            onMatch: function(instance) {
                instance.chall04("frida")
            },
            onComplete: function() {}
        });
    }) 
})