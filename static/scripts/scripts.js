$(document).ready(function () {

    if ($(document).attr('title') == "Woodland Heath Golf Club") {
        $("#home").addClass("active");
    } else if ($(document).attr('title') == "Woodland Heath Golf Club - Login") {
        $("#login").addClass("active");
    }
});