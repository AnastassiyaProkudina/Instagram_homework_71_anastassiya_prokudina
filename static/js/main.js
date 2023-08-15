$(document).ready(function () {
    $("body").on("click", ".manage-likes", function (e) {

        e.preventDefault();
        const postId = $(this).data("post");
        const csrfToken = $(this).data("token");
        const url = $(this).data("url");
        const like = $(this).data("like");
        const dislike = $(this).data("dislike");
        console.log(postId)

        $.ajax({
            url: url,
            type: 'POST',
            dataType: 'json',
            headers: {
                "X-CSRFTOKEN": csrfToken
            },
            data: {
                pk: postId
            },
            success: function (response) {
                console.log(response)
                if (response.like_added === true) {
                    $(".like-" + postId + " img").attr("src", dislike);
                    $(".post-likes-count-" + postId).text(response.post_likes_count + ' отметок "Нравится"');
                } else {
                    $(".like-" + postId + " img").attr("src", like);
                    $(".post-likes-count-" + postId).text(response.post_likes_count + ' отметок "Нравится"');
                }
            }
        });
        return false;
    });
});