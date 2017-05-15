function resize_stuff()
{
    const w = $(window).width();
    if(w<800) {
        $("div.nav-wrapper").width(w);
        $("div.about-text").width(w*0.8);
    }
    else { 
        $("div.nav-wrapper").width(w * 0.7);
        $("div.about-text").width(w* 0.6);
    }

    //Height of background image TODO: on resize
    var hi = $("img.bg").height(); 
    var hw = $(window).height(); 
    $("img.bg").height(hw*2.0);
    console.log($("img.bg").height());

}

$( document ).ready(function() {


    //Change heading when scrolling 
    $(window).scroll(function() {
        const pos = $(window).scrollTop();
        
        if(pos>0) {
            $("div.inner").css('padding-top','0px');
            $("div.masthead").addClass('masthead-scrolled');
            $("div.masthead").removeClass('masthead-unscrolled');

        }
        else {
            $("div.inner").css('padding-top','30px');
            $("div.masthead").addClass('masthead-unscrolled');
            $("div.masthead").removeClass('masthead-scrolled');
        }
    });

    //Set sizes on load
    resize_stuff();

    //Change element size on resize
    $(window).resize(function() {
        const w = $(window).width();
        const h = $(window).height();
        $("div.firstpage").height(h * (550/800));
        $("div.downarrow").height(h * (200/800));
        $("div.top").height(h * (150/800));
        resize_stuff();
        //alert(w+' '+h);
    });


});
