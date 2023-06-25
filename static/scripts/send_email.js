window.onload = function () {
    document.getElementById('contact-form').addEventListener('submit', function (event) {
        event.preventDefault();
        emailjs.init('DoAxVynWgzhWkHJmx');
        emailjs.send('service_bm8364c', 'online_enquiry', {
            'first_name': this.first_name.value,
            'last_name': this.last_name.value,
            'email': this.email.value,
            'message': this.message.value,
        }).then(function () {
            console.log('SUCCESS!');
        }, function (error) {
            console.log('FAILED...', error);
        });
    });
};