$(document).ready(function () {

    // function to add active page class to nav bar

    if ($(document).attr('title') == "Woodland Heath Golf Club") {
        $("#home").addClass("active");
    } else if ($(document).attr('title') == "Woodland Heath Golf Club - Login") {
        $("#login").addClass("active");
    } else if ($(document).attr('title') == "Woodland Heath Golf Club - Register") {
        $("#register").addClass("active");
    } else if ($(document).attr('title') == "Woodland Heath Golf Club - Member Zone") {
        $("#memberzone").addClass("active");
    } else if ($(document).attr('title') == "Woodland Heath Golf Club - Contact Us") {
        $("#contact").addClass("active");
    }
});

$(document).ready(function () {
    $('ul.hidden-radio input:radio').change(function () {
        // Only remove the class in the specific `box` that contains the radio
        $('li.pressed').removeClass('pressed');
        $(this).closest('li').addClass('pressed');
    });
});

$(document).ready(function () {
    // validation for user date selection to progress to next part of booking

    let date = $("#id_booking_date").val();

    $('#id_booking_date').change(function () {
        let newdate = $("#id_booking_date").val();

        if (newdate < date) {
            $("ul.hidden-radio").addClass("d-none");
            $("#error_container").removeClass("d-none");
            $("#date_error").text("Please select date from tomorrow onwards. If you would like to enquire about a booking for today, please call out Pro Shop on 01234 123123.");
            $("label[for='id_booking_time_0']").addClass("d-none");
            $("label[for='id_number_players']").addClass("d-none");
            $("#id_number_players").addClass("d-none");
            $("#booking_submit").addClass("d-none");
        } else {
            $("ul.hidden-radio").removeClass("d-none");
            $("label[for='id_number_players']").removeClass("d-none");
            $("#id_number_players").removeClass("d-none");
            $("#booking_submit").removeClass("d-none");
            $("label[for='id_booking_time_0']").removeClass("d-none");
            $("#error_container").addClass("d-none");

        }
    });
});

$(document).ready(function () {
    // add classes to style label elements of form

    $("label[for='id_booking_time_0']").css("margin-bottom", "5px");
    $("label[for='id_number_players']").css("display", "flex");
    $("label[for='id_number_players']").css("width", "auto");
    $("#id_number_players").css("width", "auto");
});


$(document).ready(function () {

    // function hide non change fields in form

    if ($("#amend_booking_title").text() == "Amend Your Booking") {
        $("label[for='id_booking_time_0']").addClass("d-none");
        $("#id_booking_time").addClass("d-none");
    }
});
