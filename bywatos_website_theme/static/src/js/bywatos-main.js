odoo.define('bywatos_website_theme.main', function (require) {
    document.addEventListener('DOMContentLoaded', function () {

        let routes = ['homepage', 'portfolio', 'workshop', 'contact-us'];

        routes.forEach(function(route){
            let divId = document.getElementById(route);

            if(divId){
                let elementMenuItem = document.getElementById('menu-item-' + route);

                if(elementMenuItem){
                    elementMenuItem.classList.add('current-menu-item');
                }
            }
        });

    });
});