$(document).ready(function () {

    if ($(document).attr('title') == "Woodland Heath Golf Club") {
        $("#home").addClass("active");
    } else if ($(document).attr('title') == "Woodland Heath Golf Club - Login") {
        $("#login").addClass("active");
    } else if ($(document).attr('title') == "Woodland Heath Golf Club - Register") {
        $("#register").addClass("active");
    }
});
//
// $(document).ready(function () {
//     $('ul.hidden-radio li').addClass("btn btn-primary active");
//     $('ul.hidden-radio li label').attr('data-toggle', 'dropdown');
// });

$(document).ready(function () {
    $('ul.hidden-radio input:radio').change(function () {
        // Only remove the class in the specific `box` that contains the radio
        $('li.pressed').removeClass('pressed');
        $(this).closest('li').addClass('pressed');
    });
});