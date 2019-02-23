odoo.define('bywatos_website_theme.main', function (require) {
    document.addEventListener('DOMContentLoaded', function () {

        var modalElement= document.getElementById('descriptionProductModal');

        function resize() {
            if(modalElement){
                positionModal(modalElement);
            }

        }

        function positionModal(modalElement){

            let modalWidth = modalElement.offsetWidth;
            let windowWidth = window.innerWidth;

            let modalLeftPosition = ((windowWidth / 2) - (modalWidth / 2));
            modalElement.style.left = modalLeftPosition + 'px';
        }

        positionModal(modalElement);
        window.onresize = resize;

    });
});