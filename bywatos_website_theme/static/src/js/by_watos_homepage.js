document.addEventListener('DOMContentLoaded', function () {

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

    if(element){
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