/**
 * Created by ilyes on 4/3/17.
 */


// Follow the user when click on the follow button
$('#follow-btn').click(function () {
    // Get the username to follow
    const username = $('#username').text();

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
        showMessage("Error when trying to follow the user " + username)
    })

});


// Unfollow the user when clicking on the unfollow button
$("#unfollow-btn").click(function () {

});
