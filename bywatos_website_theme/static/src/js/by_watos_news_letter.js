odoo.define('bywatos_website_theme.newsletter', function (require) {
    document.addEventListener('DOMContentLoaded', function () {

        var ajax = require('web.ajax');

        var submit_button = document.getElementById('submit-news-letter');

        var successElement = document.getElementById('newsletter-success');
        var errorElement = document.getElementById('newsletter-error');

        if(submit_button){
            submit_button.addEventListener('click', function(event){

                var input_value = document.getElementById('news-letter-mail').value;

                if(successElement.style.display === 'block'){
                    successElement.style.display = 'none'
                }

                if(errorElement.style.display === 'block'){
                    errorElement.style.display = 'none'
                }

                if(input_value){

                    ajax.jsonRpc(
                    '/save-mail-news-letter',
                    'call',
                    {
                        'email': input_value,
                    }).then(function(result){
                        if(result === 'error'){
                            if(errorElement){
                                errorElement.style.display = 'block';
                            }
                        }else {
                            if(successElement){
                                successElement.style.display = 'block';
                            }
                        }
                    });
                }

            });
        }
    });
});