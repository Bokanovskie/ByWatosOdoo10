odoo.define('bywatos_website_theme.by_watos', function(require) {'use strict'
    var position = $(window).scrollTop();
    console.log('------ TEST');
    // should start at 0
    $(window).scroll(function() {

        var scroll = $(window).scrollTop();
        if(scroll > position) {

            console.log('scrollDown');
        } else {
             console.log('scrollUp');

        }
        position = scroll;
    });
});
