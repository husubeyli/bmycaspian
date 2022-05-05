// index-2
<script>

    var revapi4,
    tpj;
jQuery(function () {
   tpj = jQuery;
   if (tpj("#rev_slider_4_1").revolution == undefined) {
      revslider_showDoubleJqueryError("#rev_slider_4_1");
   } else {
      revapi4 = tpj("#rev_slider_4_1").show().revolution({
         jsFileLocation: "js/",
         sliderLayout: "fullwidth",
         visibilityLevels: "1240,1024,778,480",
         gridwidth: "1300,1024,778,480",
         gridheight: "900,709,539,333",
         spinner: "spinner0",
         editorheight: "900,709,539,333",
         responsiveLevels: "1240,1024,778,480",
         disableProgressBar: "on",
         navigation: {
            onHoverStop: false,
            bullets: {
               enable: true,
               tmp: "<span class=\"tp-bullet-inner\"></span>",
               style: "uranus"
            }
         },
         fallbacks: {
            allowHTML5AutoPlayOnAndroid: true
         },
      });
   }

});
</script>

// index-3

<script>

        var revapi6,
        tpj;
jQuery(function () {
        tpj = jQuery;
   if (tpj("#rev_slider_6_1").revolution == undefined) {
        revslider_showDoubleJqueryError("#rev_slider_6_1");
   } else {
        revapi6 = tpj("#rev_slider_6_1").show().revolution({
            jsFileLocation: "js/",
            sliderLayout: "fullwidth",
            visibilityLevels: "1240,1024,778,480",
            gridwidth: "1300,1024,778,480",
            gridheight: "900,709,539,333",
            spinner: "spinner0",
            editorheight: "900,709,539,333",
            responsiveLevels: "1240,1024,778,480",
            disableProgressBar: "on",
            navigation: {
                onHoverStop: false,
                arrows: {
                    enable: true,
                    tmp: "<div class=\"tp-arr-allwrapper\"> <div class=\"tp-arr-imgholder\"></div></div>",
                    style: "hades",
                    hide_onmobile: true,
                    hide_under: "1499px",
                    left: {
                        h_offset: 0
                    },
                    right: {
                        h_offset: 0
                    }
                },
                bullets: {
                    enable: true,
                    tmp: "",
                    style: "hermes",
                    hide_over: "1499px"
                }
            },
            fallbacks: {
                allowHTML5AutoPlayOnAndroid: true
            },
        });
   }

});
</script>