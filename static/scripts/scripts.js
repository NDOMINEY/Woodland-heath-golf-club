$(document).ready(function () {

    if ($(document).attr('title') == "Woodland Heath Golf Club") {
        $("#home").addClass("active");
    } else if ($(document).attr('title') == "Woodland Heath Golf Club - Login") {
        $("#login").addClass("active");
    } else if ($(document).attr('title') == "Woodland Heath Golf Club - Register") {
        $("#register").addClass("active");
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
    let date = $("#id_booking_date").val();

    $('#id_booking_date').change(function () {
        let newdate = $("#id_booking_date").val();

        if (newdate < date) {
            $("ul.hidden-radio").addClass("d-none");
            $("#error_container").removeClass("d-none");
            $("#date_error").text("Please select date from tomorrow onwards...");
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

// Function to filter out booked time slots
$(document).ready(function () {
    $('ul.hidden-radio input:radio').each(function () {
        if ($(this).attr('value') == "08:00") {
            $(this).closest('li').addClass("d-none");
        };

    });

    // find('label').each(function (i) {
    //     if ($(this).text.includes(" 08:00")) {
    //         $(this).addClass("d-none");
    //     }
    // });
});