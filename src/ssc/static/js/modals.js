/**
 * Created by moreka on 10/5/14 AD.
 */

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(function() {
    /**
     * Register button :click
     */

    $("#site-register").click(function() {
        var passwd = $("#user-password").val();
        var passwd_repeat = $("#user-password-repeat").val();

        if (passwd !== passwd_repeat) {
            toastr["error"]("رمز عبور و تکرار آن یکی نمی‌باشند");
            return;
        }

        var request = $.ajax({
            url: '/register_site',
            type: 'POST',
            data: {
                studentID: $("#user-studentID").val(),
                username: $("#user-username").val(),
                mail: $("#user-mail").val(),
                password: passwd
            }
        });
        request.done(function(response) {
            console.log("Done", response);
            var data = JSON.parse(response);
            if (data.status == 'fail') {
                toastr["error"](data.message);
            }
            if (data.status == 'success') {
                toastr["success"](data.message);
                $("#regModal").modal('hide');
            }
        });
        request.fail(function(response) {
            console.log("Fail", response);
            toastr["error"]('خطا');
        });
    });

    $("#site-login").click(function() {
        var username = $("#login-username").val();
        var passwd = $("#login-password").val();
        var csrf = getCookie('csrftoken');

        var request = $.ajax({
            url: '/login_site',
            type: 'POST',
            data: {
                username: username,
                password: passwd,
                csrfmiddlewaretoken: csrf
            },
            headers: {
                'X-CSRFToken': csrf
            }
        });
        request.done(function(response) {
            console.log("Done", response);
            var data = JSON.parse(response);
            if (data.status == 'fail') {
                toastr["error"](data.message);
            }
            if (data.status == 'success') {
                toastr["success"](data.message);
                $("#loginModal").modal('hide');
                window.setTimeout(function() { location.reload(); }, 1000);
            }
        });
        request.fail(function(response) {
            console.log("Fail", response);
        });
    });
});