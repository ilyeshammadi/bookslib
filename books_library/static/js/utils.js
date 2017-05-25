/**
 * Created by ilyes on 4/5/17.
 */
/**
 * Function to show message
 */
const ALERT_SUCCESS = "alert-success";
const ALERT_INFO = "alert-info";
const ALERT_WARNING = "alert-warning";
const ALERT_DANGER = "alert-danger";


function showMessage(message, type=ALERT_SUCCESS, hide=true) {
    const HTMLalertMessage = "<div id='dj-message' class='alert " + type + "'>" + message + "</div>";
    $('#messages').append(HTMLalertMessage);

    // Remove the message after 5 seconds
    if (hide) removeMessages();
}


/**
 * Function to remove the message that
 * are created by the showMessage of the django messages
 */
function removeMessages() {
    setTimeout(function () {
        const $target = $('.alert');
        $target.hide('slow', function () {
            $target.remove();
        });
    }, 5000);
}


function showSnackbar(message) {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar");

    // Set the content
    x.innerHTML = message;

    // Add the "show" class to DIV
    x.className = "show";

    // After 3 seconds, remove the show class from DIV
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}
