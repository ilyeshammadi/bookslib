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


async function sharePromise() {
    return await $.get('/books/share/' + bookId);
}

function share(share) {
    const link = share + window.location.href;
    window.location.href = link;
}

function facebookShare() {
    const shareURL = "https://www.facebook.com/sharer/sharer.php?u=";
    share(shareURL);
}

function twitterShare() {
    const shareURL = "https://twitter.com/home?status=";
    share(shareURL);
}

function linkedinShare() {
    const shareURL = "https://www.linkedin.com/shareArticle?mini=true&url=";
    share(shareURL);
}

$('#facebook').click(function () {
    sharePromise().then(function () {
        facebookShare();
    });
});


$('#twitter').click(function () {
    sharePromise().then(function () {
        twitterShare();
    });
});

$('#linkedin').click(function () {
    sharePromise().then(function () {
        linkedinShare();
    });
});


$('.notification').click(function (e) {

    const $notification = $(e.target);
    const noti_id = $notification.attr('id');

    //Set the notification as viewed
    $.get('/navigation/notification/viewed/' + noti_id).done(function () {
        setTimeout(function () {
            $notification.addClass('noti-viewed');
        }, 2000);
        console.log('viewed')
    });



});
