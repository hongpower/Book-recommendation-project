$(function(){
        var userId= $('#my-info>div>a').text()

        $.ajax({
            url: "/mysite/all_wish/mysite_wishlistbook",
            data: {'user_id': userId},
            success: function (data) {

                wishBookImgStr=''
                str = ''

                data=data['books']

                for(var i =0;i<data.length;i++){
                        wishBookImgStr += "<div class='book-img-container' id='mysite-wishlist'"+i+">"
                        wishBookImgStr += "<img class='book-img'  src=" + data[i].cover_large + " name=" + data[i].book_id+ ">"
                        wishBookImgStr += '<span><i class="fas fa-heart wishlist-btn btns fa-2x" style="position: absolute; top: 85%; left: 80%; z-index: 30"></i></span>'
                        wishBookImgStr += '<span><i class="fas fa-thumbs-up like-btn btns fa-2x" style="position: absolute; top: 70px; left: 80px; z-index: 30"></i></span>'
                        wishBookImgStr += '<span><i class="fas fa-thumbs-down dislike-btn btns fa-2x" style="position: absolute; top: 160px; left: 80px; z-index: 30"></i></span>'
                        wishBookImgStr += "</div>"
                }


                $(".wish-img-article").html(wishBookImgStr);
            }
        })

    })