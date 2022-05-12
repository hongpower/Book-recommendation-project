$(function(){
    //토픽 클릭하면 클래스 주기
//    $(".topic").click(function(){
//
//        $(this).toggleClass('in-topics')
//    })
    $(".topic-box").on("click",'.topic', function(e){
        $(e.target).toggleClass('in-topics')
    })

    $(".start-rcm-btn").click(function(){
        // in-topics인 topic들을 가져온다
        topicAry = []
        $(".in-topics").each(function(index, obj){
            topicAry.push($(this).text())
        })

         $(".swiper-wrapper").empty()
         $("h3").remove()
         // 내일 좋아요 싫어요 삭제하는 코드 여기 추가!!!

        $.ajax({
            url: "/recommendation/get_topic_rcm",
            data: {'topic_lst' : topicAry, 'user_id': userId},
            dataType: 'json',
            success: function(data){
                userId = data['user_id']
                data = data['topic_books']


                $("#rcm-books").prepend("<h3>"+userId+"님이 선호하는 키워드의 도서들로 구성해봤어요!</h3>")
                str = ""
                for(var i=0; i<data.length; i++){
                    var book_set = data[i]
                    str += "<div class='swiper-slide'>"

                    for(var j=0; j<book_set.length; j++){
                        var book = book_set[j]
                        var coverLarge = book.img_url
                        var bookId = book.book_id

                        str += "<div class='book-img-container'>"
                        str += "<img class='book-img'  src=" + coverLarge + " name=" + bookId+ ">"
                        str += "<span><i class='fas fa-heart wishlist-btn btns fa-2x' style='position: absolute; top: 85%; left: 80%; z-index: 30'></i></span>"
                        str += "<span><i class='fas fa-thumbs-up like-btn btns fa-3x' style='position: absolute; top: 70px; left: 80px; z-index: 30'></i></span>"
                        str += "<span><i class='fas fa-thumbs-down dislike-btn btns fa-3x' style='position: absolute; top: 160px; left: 80px; z-index: 30'></i></span>"

                        str += "</div>"
                    }
                    str += "</div>"

                }

                $(".swiper-wrapper").append(str)

                var buttonStr = ""
                buttonStr += '<div class="swiper-button-next"></div>'
                buttonStr += '<div class="swiper-button-prev"></div>'

                //$(".swiper-button-prev").removeClass("swiper-button-disabled")
                //$(".swiper-button-next").removeClass("swiper-button-disabled")
                $(".")
//                $(".swiper-container").append(buttonStr)
            }
        })
    })

    $(".refresh-btn").on("click", function(){

        $.ajax({
            url: "/recommendation/get_topic_refresh",
            dataType: 'json',
            success: function(data){
                data = data['topic_lst']
                console.log(data)
                str = ""

                $(".topic-box").empty()

                for(var i=0; i<data.length; i++){
                    var topic = data[i]
                    str += "<span class='topic'>" + topic + "</span>"

                    }

                $(".topic-box").append(str)
            }

        })
    })

})