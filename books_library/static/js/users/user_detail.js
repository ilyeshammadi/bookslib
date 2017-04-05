/**
 * Created by ilyes on 4/3/17.
 */

const HTMLunfollowButton = '<button id="unfollow-btn" class="btn btn-default btn-follow">Unfollow</button>';
const HTMLfollowButton = '<button id="follow-btn" class="btn btn-default btn-follow">Follow</button>';


// Follow the user when click on the follow button
function follow(username) {
// Send the username to the server
    $.get("/users/follow/" + username)
        .done(function () {

            // Change the id to unfollow
            $('#follow-btn').attr({
                id: "unfollow-btn"
            })
            // Change the text to unfollow
                .text("Unfollow");


            showMessage("You just follwed " + username + " Congratulations !!");

        }).fail(function () {
        showMessage("Error when trying to follow the user " + username, ALERT_DANGER)
    })
}

// Unfollow the user when clicking on the unfollow button
function unfollow(username) {
// Send the username to the server
    $.get("/users/unfollow/" + username)
        .done(function () {

            // Change the id to follow
            $('#unfollow-btn').attr({
                id: "follow-btn"
            })
            // Change the text to follow
                .text("Follow");


            showMessage("You just unfollwed " + username, ALERT_INFO);

        }).fail(function () {
        showMessage("Error when trying to follow the user " + username, ALERT_DANGER)
    })
}


$('#follow-btn, #unfollow-btn').click(function () {
    // Get the username to follow
    const username = $('#username').text();
    const text = $("#follow-btn, #unfollow-btn").text();

    if(text === "Follow") {
        follow(username);
    } else if (text === "Unfollow"){
        unfollow(username);
    }

});

