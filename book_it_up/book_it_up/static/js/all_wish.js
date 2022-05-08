$(function(){


        var user_id = $(".card>h1").text()

        $.ajax({
            url: "/mysite/all_wish/mysite_wishlistbook",
            data: {'user_id': user_id},
            success: function (data) {

                wishBookImgStr=''
                str = ''

                data=data['books']

                for(var i =0;i<data.length;i++){
                        wishBookImgStr += "<div class='book-img-container' id='mysite-wishlist'"+i+">"
                        wishBookImgStr += "<img class='book-img'  src=" + data[i].cover_large + " name=" + data[i].book_id+ ">"
                        wishBookImgStr += "</div>"
                }


                $(".wish-img-article").html(wishBookImgStr);
            }
        })

    })