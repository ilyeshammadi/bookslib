/**
 * Created by ilyes on 5/11/17.
 */
function showForm() {
    $('#comment-form').css({
        display: 'block'
    });

    $('#show-comment').css({
        display: 'none'
    });

}

function hideForm() {
    $('#comment-form').css({
        display: 'none'
    });

    $('#show-comment').css({
        display: 'inline-block'
    });

}


// Hide the form bu default
hideForm();


$('#show-comment').click(function () {
    showForm();
});

$('#cancel').click(function () {
   hideForm();
});
