/* Project specific Javascript goes here. */

/*
 Formatting hack to get around crispy-forms unfortunate hardcoding
 in helpers.FormHelper:

 if template_pack == 'bootstrap4':
 grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
 using_grid_layout = (grid_colum_matcher.match(self.label_class) or
 grid_colum_matcher.match(self.field_class))
 if using_grid_layout:
 items['using_grid_layout'] = True

 Issues with the above approach:

 1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
 2. Unforgiving: Doesn't allow for any variation in template design
 3. Really Unforgiving: No way to override this behavior
 4. Undocumented: No mention in the documentation, or it's too hard for me to find
 */
$('.form-group').removeClass('row');


let xhr = null;
const $searchBar = $('#search-bar');
const $searchResults = $('#search-results');

function closeResultList() {
    $searchBar.removeClass('open');
    $searchResults.html('');
}


function openResultList() {
    $searchResults.css({
        width: '30vw'
    });

    $searchBar.addClass('open')
}

function search(searchTerms) {
    // Stop any prevoius AJAX call
    if (xhr !== null) {
        xhr.abort();
        xhr = null;
    }


    // Search terms is empty close the search result list
    if (!searchTerms.length > 0) {
        console.log('Empty');
        closeResultList();
    } else {
        xhr = $.ajax({
            type: "GET",
            url: "/api/search/",
            data: "search=" + searchTerms,
            success: function (data) {
                // Open dropdown
                if (!$searchBar.hasClass('open')) {
                    openResultList();
                }

                // Clean the search results from prevouis data
                $searchResults.html('');

                // If there are results show them
                // Otherwise close the list
                if (data.results.length > 0) {
                    data.results.forEach(function (item) {
                        // Append data here
                        $searchResults.append('<li><a href="/books/detail/' + item.slug + '">' + item.name + '</a></li>')
                    })
                } else {
                    closeResultList();
                }
            }
        });
    }


}


$("#search-bar").find("input").on('change paste keyup', function () {
    const searchTerms = $(this).val();
    console.log(searchTerms);

    setTimeout(function () {
        search(searchTerms);
    }, 300);


});
