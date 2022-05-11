$(function(){

        var userId= $('#my-info>div>a').text()

        $.ajax({
            url: "/mysite/all_like/mysite_likebook",
            data: {'user_id': userId},
            success: function (data) {

                likeBookImgStr=''
                str = ''

                data=data['books']
                for(var i =0;i<data.length;i++){
                        likeBookImgStr += "<div class='book-img-container' id='mysite-like'"+i+">"
                        likeBookImgStr += "<img class='book-img'  src=" + data[i].cover_large + " name=" + data[i].book_id+ ">"
                        likeBookImgStr += '<span><i class="fas fa-heart wishlist-btn btns fa-2x" style="position: absolute; top: 85%; left: 80%; z-index: 30"></i></span>'
                        likeBookImgStr += '<span><i class="fas fa-thumbs-up like-btn btns fa-2x" style="position: absolute; top: 70px; left: 80px; z-index: 30"></i></span>'
                        likeBookImgStr += '<span><i class="fas fa-thumbs-down dislike-btn btns fa-2x" style="position: absolute; top: 160px; left: 80px; z-index: 30"></i></span>'
                        likeBookImgStr += "</div>"
                }

//                console.log(likeBookImgStr)
                $(".like-img-article").html(likeBookImgStr);
                // 좋아요는 다 미리 눌려져서 나오기
                $(".like-btn").toggleClass('in_likes')
            }
        })

    })