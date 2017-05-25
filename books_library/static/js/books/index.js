function like(bookId, $book) {
    $.get("/books/like/" + bookId)
        .done(function (res) {

            // Change the heart icon state to filled
            $book.addClass('fa-heart');
            $book.removeClass('fa-heart-o');

            $book.removeClass('like');
            $book.addClass('dislike');

            // Update the likes
            $("#likes-count-" + bookId).text(res.likes);


        }).fail(function (err) {
        showMessage(err, ALERT_DANGER);
    })
}

function dislike(bookId, $book) {
    $.get("/books/dislike/" + bookId)
        .done(function (res) {

            // Change the heart icon state to filled
            $book.addClass('fa-heart-o');
            $book.removeClass('fa-heart');

            $book.removeClass('dislike');
            $book.addClass('like');

            // Update the likes
            $("#likes-count-" + bookId).text(res.likes);


        }).fail(function (err) {
        showMessage(err, ALERT_DANGER);
    })
}

$('.like, .dislike').click(function (e) {
    // Get the cliked item object
    const $book = $(e.target);

    // Get the id from the id attribute
    const bookId = $book.attr('id').split('-')[1];

    if ($book.hasClass('like')) {
        like(bookId, $book);
    } else if($book.hasClass('dislike')) {
        dislike(bookId, $book);
    }


});


function bookmark(bookId, $book) {
    $.get("/books/bookmark/" + bookId)
        .done(function (res) {

            // Change the heart icon state to filled
            $book.addClass('fa-bookmark');
            $book.removeClass('fa-bookmark-o');

            $book.removeClass('bookmark');
            $book.addClass('unbookmark');

            showSnackbar('Item bookmarked');

        }).fail(function (err) {
        showMessage(err, ALERT_DANGER);
    })
}

function unbookmark(bookId, $book) {
    $.get("/books/unbookmark/" + bookId)
        .done(function (res) {

            // Change the heart icon state to filled
            $book.addClass('fa-bookmark-o');
            $book.removeClass('fa-bookmark');

            $book.removeClass('unbookmark');
            $book.addClass('bookmark');


        }).fail(function (err) {
        showMessage(err, ALERT_DANGER);
        console.log(err);
    })
}

$('.bookmark, .unbookmark').click(function (e) {
    // Get the cliked item object
    const $book = $(e.target);

    // Get the id from the id attribute
    const bookId = $book.attr('id').split('-')[1];

    if ($book.hasClass('bookmark')) {
        bookmark(bookId, $book);
    } else if($book.hasClass('unbookmark')) {
        unbookmark(bookId, $book);
    }


});
