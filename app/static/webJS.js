
            $(function() {
                $(window).scroll( function(){


                    $('.fadeInBlock').each( function(i){

                        var bottom_of_object = $(this).position().top + $(this).outerHeight();
                        var bottom_of_window = $(window).scrollTop() + $(window).height();

                        /* Adjust the "200" to either have a delay or that the content starts fading a bit before you reach it  */
                        bottom_of_window = bottom_of_window + 100;

                        if( bottom_of_window > bottom_of_object ){

                            $(this).animate({'opacity':'1'},500);
                        }
                    });

                });
            });

            function scaleToFill() {
                $('video.video-background').each(function(index, videoTag) {
                   var $video = $(videoTag),
                       videoRatio = videoTag.videoWidth / videoTag.videoHeight,
                       tagRatio = $video.width() / $video.height(),
                       val;

                   if (videoRatio < tagRatio) {
                       val = tagRatio / videoRatio * 1.02; <!-- size increased by 2% because value is not fine enough and sometimes leaves a couple of white pixels at the edges -->
                   } else if (tagRatio < videoRatio) {
                       val = videoRatio / tagRatio * 1.02;
                   }

                    $video.css('transform','scale(' + val  + ',' + val + ')');

                });
            }

            $(function () {
                scaleToFill();

            $('.video-background').on('loadeddata', scaleToFill);

            $(window).resize(function() {
                scaleToFill();
            });
        });



        jQuery(function($){
             $( '.menu-btn' ).click(function(){
             $('.responsive-menu').toggleClass('expand')
             })
        })




