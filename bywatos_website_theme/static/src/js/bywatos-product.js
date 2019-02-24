odoo.define('bywatos_website_theme.main', function (require) {
    document.addEventListener('DOMContentLoaded', function () {

        // Product description modal
        var modalElement = document.getElementById('description-product-modal');

        // Button to display modal
        var continuousButton = document.getElementById('continuous-button');

        // Button to close modal
        var closeButtonModal = document.getElementById('close-button-modal');


        if(continuousButton && modalElement && closeButtonModal){

            // Add event click listener on continuous button to open modal
            continuousButton.addEventListener('click', () => {

                modalElement.classList.remove('hidden');
                modalElement.classList.add('show');
                
                positionModal(modalElement);

            });

            // Add event click listener on continuous button to close modal
            closeButtonModal.addEventListener('click', () => {

                modalElement.classList.remove('show');
                modalElement.classList.add('hidden');

            });
        }

        // Function execute on page resize
        function resize() {
            if(modalElement){
                positionModal(modalElement);
            }

        }

        // Function to position the modal
        function positionModal(modalElement){

            let modalWidth = modalElement.offsetWidth;
            let windowWidth = window.innerWidth;

            let modalHeight = modalElement.offsetHeight;
            let windowHeight = window.innerHeight;

            let modalXPosition = ((windowWidth / 2) - (modalWidth / 2));
            let modalYPosition = ((windowHeight / 2) - (modalHeight / 2));

            modalElement.style.left = modalXPosition + 'px';
            modalElement.style.top = modalYPosition + 'px';
        }

        positionModal(modalElement);

        modalElement.classList.remove('show');
        modalElement.classList.add('hidden');

        window.onresize = resize;

    });
});