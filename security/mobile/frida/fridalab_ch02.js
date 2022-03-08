setImmediate(function() {
    Java.perform(function() {
        /* private로 선언되어있기 때문에 use 사용 불가. */
        Java.choose("uk.rossmarks.fridalab.MainActivity", {
            onMatch: function(instance) {
                instance.chall02()
            },
            onComplete: function() {

            }
        })
    }) 
})