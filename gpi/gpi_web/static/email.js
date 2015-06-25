window.onload = function() {
    submit = document.getElementById('email_submit');
    submit.onclick = sendEmail;
}

function processEmail() {
    var result = JSON.parse(this.responseText);
    if(result.status) {
        var success_box = document.createElement('div');
        var message = document.createTextNode('Thanks for signing up!');
        success_box.appendChild(message);
        success_box.id = 'message';
        var email_container = document.getElementById('email_container');
        email_container.appendChild(success_box);
        document.getElementById('email').remove();
    }

    else {
        if (document.getElementById('message')) {
            document.getElementById('message').innerHTML = result.errortext;
        } else {
            var failbox = document.createElement('div');
            var message = document.createTextNode(result.errortext);
            failbox.appendChild(message);
            failbox.id = 'message';
            var email = document.getElementById('email');
            email.appendChild(failbox);
        }
    }
}

function sendEmail() {
    csrf_token = document.getElementById('csrf_token').value;
    email_address = document.getElementById('email_box');
    request = new XMLHttpRequest();
    request.onload = processEmail;
    request.open('POST', '/add_email?email=' + email_address.value);
    request.setRequestHeader('X-CSRFToken', csrf_token);
    request.send();
}
