/**
 * Created by moreka on 10/5/14 AD.
 */

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
                toastr["error"](data.error);
            }
        });
        request.fail(function(response) {
            console.log("Fail", response);
        });
    });
});