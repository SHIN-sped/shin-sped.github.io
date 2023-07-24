function submitForm(event) {
    event.preventDefault();

    var username = document.getElementsByName('username')[0].value;
    var password = document.getElementsByName('username')[0].value;

    var url = "3_form_res.html?username=" + username + "&password=" + password;
    window.location.href = url;
}
