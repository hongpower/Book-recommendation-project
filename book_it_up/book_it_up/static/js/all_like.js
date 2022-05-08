$(function(){

        $(".like-img-aricle").empty()
        var user_id = $(".card>h1").text()

        $.ajax({
            url: "/mysite/all_like/mysite_likebook",
            data: {'user_id': user_id},
            success: function (data) {

                likeBookImgStr=''
                str = ''

                data=data['books']
                for(var i =0;i<data.length;i++){
                        likeBookImgStr += "<div class='book-img-container' id='mysite-like'"+i+">"
                        likeBookImgStr += "<img class='book-img'  src=" + data[i].cover_large + " name=" + data[i].book_id+ ">"
                        likeBookImgStr += "</div>"
                }

//                console.log(likeBookImgStr)
                $(".like-img-aricle").html(likeBookImgStr);
            }
        })

    })