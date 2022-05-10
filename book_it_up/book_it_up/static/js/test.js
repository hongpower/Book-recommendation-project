$(function(){
    $.ajax({
        url: "/test/getbook",
        data:{'first':'first'},
        dataType: 'json',
        success: function (data) {
            data=data['books']
            data=data[0]

            var bookImageStr=''

            var bookId=data.book_id
            var coverLarge=data.cover_large

            bookImageStr += "<img class='book-img' src=" + coverLarge + " name=" + bookId+ ">"

            console.log(bookImageStr)
            $(".book-img").remove()
            $('.book-img-container').prepend(bookImageStr);
        }
    })
    $(".btn").on("click", function(){
        var btnType = $(this).attr("id")
        var bookId = $(".book-img").attr("name")
        getAnotherBook(bookId, btnType)
    })
})

function getAnotherBook(bookId,btnType){
    $.ajax({
        url: "/test/getbook",
        data: {'user_id': userId,'book_id':bookId,'btn_type':btnType},
        success: function (data) {
            data=data['books']
            data=data[0]

            var bookImageStr=''

            var bookId=data.book_id
            var coverLarge=data.cover_large

            bookImageStr += "<img class='book-img'  src=" + coverLarge + " name=" + bookId+ ">"
            $(".book-img").remove()
            $('.book-img-container').prepend(bookImageStr);
            $('.wishlist-btn').removeClass('in_wishlist')
            $('.like-btn').removeClass('in_likes')
            $('.dislike-btn').removeClass('in_dislikes')
        }
    })
}
