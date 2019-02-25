(function($) {
    "use strict";
    $(document).ready(function() {


        $(window).scroll(function () {
            if ($(window).scrollTop() >= 1) {
                $('.lc-navbar-xone').addClass('lc-navbar-xone-fixed');
            }
            else {
                $('.lc-navbar-xone').removeClass('lc-navbar-xone-fixed');
            }
        });

        /* -----------------------------------------------------
            Navbar
        ----------------------------------------------------- */
        $( "#lcnavbar" ).superMegaMenu(); 


        /* -----------------------------------------------------
            Multiple img upload
        ----------------------------------------------------- */
        $('input[type="file"]').imageuploadify();

        $(".lc-select-input-field > select").select2({
            theme: "lc-select-input-field-text"
        });

        /*-------------------------------------------
          Multi Search Auto Location
        -------------------------------------------*/
        var inputSearch = function (arg){
            document.onclick = function(e){
                if(e.target.id !== 'category_search'){
                    $('ul.category-dropdown').slideUp(300);
                }
                if(e.target.id !== 'category_search_two'){
                    $('ul.category-dropdown-two').slideUp(300);
                }
            };
            $(arg.selector).on('keyup keypress', function(e){
                var filter, a, i;
                filter = this.value.toUpperCase();
                $(arg.dropdown).slideDown(300);
                a = $(arg.dropdown + ' li');
                for (i = 0; i < a.length; i++) {
                    if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
                        a[i].style.display = "";
                        $(a[i]).addClass('detected');
                    } 
                    else {
                        $(a[i]).removeClass('detected');
                        a[i].style.display = "none";
                    }
                }
                if(e.which == 13){
                    if($(arg.dropdown + ' li.detected').length == 1){
                        var detectedValue = $(arg.dropdown + ' li.detected a').text();
                        $(arg.selector).val(detectedValue);
                        $(arg.dropdown).slideUp(300);
                    }
                }
            });
            $(arg.selector).on('click', function(e){ 
                if($(arg.selector).val() == ''){
                    $(arg.dropdown).slideDown(300);
                }
            });
            $(arg.dropdown + ' li a').on('click', function (e) {
                e.preventDefault();
                $(arg.selector).val(this.innerText);
                $(arg.dropdown).slideUp(300);
                $(arg.dropdown + ' li').css({'display' : 'none'});
                $(this).addClass('detected');
            });
        };
        if($('#category_search').length > 0){
          inputSearch({
            selector: '#category_search',
            dropdown: 'ul.category-dropdown',
          });
        }
         if($('#category_search_two').length > 0){
          inputSearch({
            selector: '#category_search_two',
            dropdown: 'ul.category-dropdown-two',
          });
        }

        /* -----------------------------------------------------
            lc toggle btn
        ----------------------------------------------------- */
        //widget opening hour
        $('.widget-opening-hour > .title').on('click', function(){
           $('.widget-opening-hour > .hidden-time').slideToggle('slow');
            $(this).toggleClass("actives");
        });
        //additional info
        $('.widget-additional-info > .toggle-btn').on('click', function(){
            $('.widget-additional-info > .additional-details-hide').slideToggle("slow");
            $(this).toggleClass("actives");
        });
        //search more filter
        $('.lc-search-more-filter-btn.lc-common-btn').on('click', function(){
            $('.lc-search-morefilter-area').slideToggle("slow");
            $(this).toggleClass("actives");
        });
        //search map hide btn
        $('.search-layout .lc-search-map-hide').on('click', function(){
            $('.lc-search-map').slideToggle("slow");
            $(this).toggleClass("actives");
        });


        /* -----------------------------------------------------
            Isotope
        ----------------------------------------------------- */
        function initIsotope() {
            if ($(".lc-gallery-wrap").length) {
                var a = $(".lc-gallery-wrap").isotope({
                    singleMode: true,
                    columnWidth: ".lc-gallery-item-small, .lc-gallery-item-large",
                    itemSelector: ".lc-gallery-item",
                    transformsEnabled: true,
                    transitionDuration: "700ms",
                    resizable: true,
                });
                a.imagesLoaded(function () {
                    a.isotope("layout");
                });
                // $(".gallery-filters").on("click", "a.gallery-filter", function (b) {
                //     var c = $(this).attr("data-filter"),
                //         d = $(this).text();
                //     b.preventDefault();
                //     var c = $(this).attr("data-filter");
                //     a.isotope({
                //         filter: c
                //     });
                //     $(".gallery-filters a.gallery-filter").removeClass("gallery-filter-active");
                //     $(this).addClass("gallery-filter-active");

                // });
            }
        }
        initIsotope();


        /* -----------------------------------------------------
            counter-up
        ----------------------------------------------------- */
        $('.counter').counterUp({
            delay: 10,
            time: 1000
        });
         
        /* -----------------------------------------------------
            Variables
        ----------------------------------------------------- */
        var leftArrow = '<i class="fa fa-angle-left"></i>';
        var rightArrow = '<i class="fa fa-angle-right"></i>';

        /* -----------------------------------------------------
           testimonial-carousel
        ----------------------------------------------------- */
        $('.lc-testimonial-carousel').owlCarousel({
            loop:true,
            margin:0,
            nav:false,
            items: 1,
        }); 

        $('.lc-testimonial-carousel-two').owlCarousel({
            loop:true,
            margin:30,
            nav:false,
            dots: true,
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:2
                },
                1000:{
                    items:3
                }
            }
        })

        /* -----------------------------------------------------
            lc-gallery-slider
        ----------------------------------------------------- */
        $('.lc-gallery-slider').owlCarousel({
            loop:false,
            margin:15,
            nav:true,
            dots: false,
            navText: [ leftArrow, rightArrow],
            responsive:{
                0:{
                    items:2
                },
                600:{
                    items:3
                },
                1000:{
                    items:4
                }
            }
        })
        /* -----------------------------------------------------
            lc-gallery-slider
        ----------------------------------------------------- */
        $('.lc-video-slider').owlCarousel({
            loop:true,
            margin:15,
            nav:true,
            dots: false,
            navText: [ leftArrow, rightArrow],
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:2
                },
                1000:{
                    items:3
                }
            }
        })
        
        /* -----------------------------------------------------
           Wow js
        ----------------------------------------------------- */
        new WOW().init();


        /* -----------------------------------------------------
           Popup modal content
        ----------------------------------------------------- */
        $('.lc-event-single a[data-toggle="modal"]').on('click', function(e){
            e.preventDefault;
            // update modal header with contents of button that invoked the modal
            var lcComponent = $(this).closest('.lc-event-single').clone();
            //fixes a bootstrap bug that prevents a modal from being reused
            $('.lc-popup-listing-view').html(lcComponent);
        });
        $('.lc-listing-single a[data-toggle="modal"]').on('click', function(e){
            e.preventDefault;
            // update modal header with contents of button that invoked the modal
            var lcComponent = $(this).closest('.lc-listing-single').clone();
            //fixes a bootstrap bug that prevents a modal from being reused
            $('.lc-popup-listing-view').html(lcComponent);
        });



        /* -------------------------------------------------------------
            MAGNIFIC JS
        ------------------------------------------------------------- */
        $('.play-video').magnificPopup({
          type: 'iframe'
        });
        $.extend(true, $.magnificPopup.defaults, {
          iframe: {
            patterns: {
              youtube: {
                index: 'youtube.com/', 
                id: 'v=', 
                src: 'http://www.youtube.com/embed/%id%?autoplay=1' 
              }
            }
          }
        });

        /* -------------------------------------------------------------
            Back to top
        ------------------------------------------------------------- */
        $(window).scroll(function(){
            if ($(this).scrollTop()>10) {
                $('#lc-toTop').addClass('backtop-top-show');
            } else {
                $('#lc-toTop').removeClass('backtop-top-show');
            }
        })
        $("#lc-toTop").on('click',function (e) {
            e.preventDefault();
           $("html, body").animate({scrollTop: 0}, 1000);
        });

        /* -------------------------------------------------------------
            Grid Change
        ------------------------------------------------------------- */
        if($('.search-layout').length > 0){
            $('.lc-search-list').on('click', function (e) {
                e.preventDefault();
                $('.listSingle').removeClass('active');
                $(this).addClass('active');
                $('.lc-search-grid').removeClass('active');
                $('.lc-listing-single').parent().addClass('col-12 lc-list-view').removeClass('col-lg-6 col-md-6');
            });
            $('.lc-search-grid').on('click', function (e) {
                e.preventDefault();
                $('.listGrid').removeClass('active');
                $(this).addClass('active');
                $('.lc-search-list').removeClass('active');
                $('.lc-listing-single').parent().addClass('col-12 col-lg-6 col-md-6').removeClass('col-12 lc-list-view');
            })
        }

        /* -------------------------------------------------------------
            Add Business Hour
        ------------------------------------------------------------- */
        if($('.lc-business-hour').length > 0){
            $('.timepicker').wickedpicker();
            // add new business hour
            $('.lc-add-new-business-hour-handler').on('click', function(e){
                e.preventDefault();
                var htmlData = '<li>'+
                '<span class="dayname">'+$('.days').children("option:selected").val()+'</span>'+
                    '<span class="daytime">'+
                        '<span class="starthour">'+$('.starttime').val()+'</span>'+
                        '<span class="endhour">'+$('.starttime').val()+'</span>'+
                    '</span>'+
                    '<a href="#" class="removebusinesshour">Remove</a>'+
                '</li>';
                $('ul.lc-generated-hour-list').append(htmlData);
            });
            // remove business hour
            $('ul.lc-generated-hour-list').on('click', '.removebusinesshour', function(e){
                e.preventDefault();
                $(this).parent().remove();
            });
        }

        /* -------------------------------------------------------------
            tinymce js
        ------------------------------------------------------------- */
        if($('.lc-add-listing-tinymce textarea').length > 0){
            tinymce.init({
              selector: '.lc-add-listing-tinymce textarea',
              height: 143,
              plugins: 'table wordcount code',
            });
        }


        //range slider
        if($('input').length > 0){
            var $element = $('input[type="range"]');
            $element
              .rangeslider({
                polyfill: false,
                onInit: function() {
                  var $handle = $('.rangeslider__handle', this.$range);
                  updateHandle($handle[0], this.value);
                }
              })
              .on('input', function(e) {
                var $handle = $('.rangeslider__handle', e.target.nextSibling);
                updateHandle($handle[0], this.value);
              });

            function updateHandle(el, val) {
              el.textContent = val;
            }
        }

        /* -----------------------------------------------------
            swiper container
        ----------------------------------------------------- */
        if($('.swiper-container').length > 0){
            var swiper = new Swiper('.swiper-container', {
              loop: true,
              autoplayDisableOnInteraction: true,
              effect: 'coverflow',
              grabCursor: true,
              centeredSlides: true,
              slidesPerView: 'auto',
              initialSlide: 2,
              coverflowEffect: {
                rotate: 0,
                stretch: 0,
                depth: 0,
                modifier: 1,
                slideShadows : true,
              },
              pagination: {
                el: '.swiper-pagination',
              },
            });
        };

        if($('.rellax').length > 0){
            if($(window).width() > 992) {
                var rellax = new Rellax('.rellax', {
                    // center: true
                    callback: function(position) {
                        // callback every position change
                    }
                });
            }
        };
        

    });
})(jQuery);


function ratingStar(event){
    var checkValue = document.querySelectorAll("input");
    var checkStar = document.querySelectorAll("label");
    var checkSmiley = document.querySelectorAll("i");
    var checkCount = 0;
    for(var i=0; i<checkValue.length; i++){
        if(checkValue[i]==event.target){
            checkCount = i+1;
        }
    }
    for(var j=0; j<checkCount; j++){
        checkValue[j].checked = true;
        checkStar[j].className = "rated";
        checkSmiley[j].style.display = "none";
    }

    for(var k=checkCount; k<checkValue.length; k++){
        checkValue[k].checked = false;
        checkStar[k].className = "check"
        checkSmiley[k].style.display = "none";  
    }
    if(checkCount == 1){
        document.querySelectorAll("i")[0].style.display = "block";
    }
    if(checkCount == 2){
        document.querySelectorAll("i")[1].style.display = "block";
    }
    if(checkCount == 3){
        document.querySelectorAll("i")[2].style.display = "block";
    }
    if(checkCount == 4){
        document.querySelectorAll("i")[3].style.display = "block";
    }
    if(checkCount == 5){
        document.querySelectorAll("i")[4].style.display = "block";
    }
}

