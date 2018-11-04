odoo.define('bywatos_website_theme.by_watos', function(require) {'use strict'

    var position = $(document).scrollTop();
    // should start at 0
    $(document).on('scroll', function() {

        var scroll = $(document).scrollTop();

        if(scroll > 250) {
            $('#sidebar').show();
        } else {
             $('#sidebar').hide();
        }
    });
});
