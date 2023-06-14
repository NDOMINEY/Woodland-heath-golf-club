$(window).scroll(function () {

    if ($(this).scrollTop() < 100) {
        $(".navbar").hide();
    } else {
        $(".navbar").show();
    }
});