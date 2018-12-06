odoo.define('bywatos_website_theme.newsletter', function (require) {
    document.addEventListener('DOMContentLoaded', function () {

        var ajax = require('web.ajax');

        var submit_button = document.getElementById('submit-news-letter');

        if(submit_button){
            submit_button.addEventListener('click', function(event){

                var input_value = document.getElementById('news-letter-mail').value;

                if(input_value){

                    ajax.jsonRpc(
                    '/save-mail-news-letter',
                    'call',
                    {
                        'email': input_value,
                    });
                }

            });
        }
    });
});