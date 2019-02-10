odoo.define('bywatos.website', function (require) {

document.addEventListener('DOMContentLoaded', function () {

    var ajax = require('web.ajax');

    var element = document.getElementById('header-bottom');
    var asideElement = document.getElementsByClassName('sidebar-homepage');
    var contactUsElement = document.getElementById('contact-us');
    var asideToggle = document.getElementById('sidebar-trigger');
    var sidebar = document.getElementById('sidebar');

    // vanilla JS window width and height
    var w=window,
    d=document,
    e=d.documentElement,
    g=d.getElementsByTagName('body')[0],
    x=w.innerWidth||e.clientWidth||g.clientWidth,
    y=w.innerHeight||e.clientHeight||g.clientHeight;

    if(element || contactUsElement){
        if(sidebar && asideElement.length > 0){
            sidebar.style.background = 'transparent';

            sidebar.addEventListener('mouseover', function(event){
                sidebar.style.background = '#333';
            });

            sidebar.addEventListener('mouseout', function(event){
                sidebar.style.background = 'transparent';
            });

        }

        if(x > 768 && asideElement.length > 0 && !contactUsElement){
            sidebar.style.display = 'none';
        }

        if(checkVisibility(element)){
            if(asideToggle){
                asideToggle.style.display = 'none';
            }
        }else {
            if(asideToggle){
                asideToggle.style.display = 'block';
            }
        }

        var mousewheelevt=(/Firefox/i.test(navigator.userAgent))? "DOMMouseScroll" : "mousewheel"

        if (document.attachEvent)
            document.attachEvent("on"+mousewheelevt, function(e){})
        else if (document.addEventListener)
            document.addEventListener(mousewheelevt, function(e){

                if(checkVisibility(element)){
                    if(asideToggle){
                        asideToggle.style.display = 'none';
                        sidebar.style.display = 'none';
                    }
                }else {
                    if(asideToggle){
                        asideToggle.style.display = 'block';
                        sidebar.style.display = 'block';
                    }
                }

            }, false)
    }

    // Get video
    ajax.jsonRpc("/get_video").then(function(data) {

        var iframeElement = document.getElementsByClassName('embed-responsive-16by9')[0];

        var iframe = document.createElement('iframe');

        iframe.setAttribute('src', data);
        iframe.setAttribute('class', 'embed-responsive-item');

        iframeElement.appendChild(iframe);

    });

});

});

function checkVisibility(element, evaluation){

    var evaluation = evaluation = evaluation || "visible";

    var viewPortHeight = window.innerHeight;
    var scrollBarPosition = window.pageYOffset | document.body.scrollTop;

    var y = element.offsetTop;

    var elementHeight = element.offsetHeight;

    if (evaluation == "visible") return ((y < (viewPortHeight + scrollBarPosition)) && (y > (scrollBarPosition - elementHeight)));
    if (evaluation == "above") return ((y < (viewPortHeight + scrollBarPosition)));
}