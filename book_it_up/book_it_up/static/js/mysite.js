//좋아요 한 도서들 이미지 가져오는 함수
$(function(){
        $(".like-img-container").empty()
        var userId= $('#my-info>div>a').text()

        $.ajax({
            url: "/mysite/mysite_likebook",
            data: {'user_id': userId},
            success: function (data) {

                likeBookImgStr='<h2>좋아요 누른책</h2>'
                str = ''

                data=data['books']
                for(var i =0;i<5;i++){
                        likeBookImgStr += "<div class='book-img-container' id='mysite-like'"+i+">"
                        likeBookImgStr += "<img class='book-img' src=" + data[i].cover_large + " name=" + data[i].book_id+ ">"
                        likeBookImgStr += "</div>"
                }


                $(".like-img-container").html(likeBookImgStr);
                // 더보기 버튼 새로 추가:
                likeBookFullButton = '<div class="full-btn"><span class="btn" id="mysite-like-btn" ><a href="/mysite/all_like">더보기</a></span></div>'
                $(".like-img-container").append(likeBookFullButton)
            }
        })

    })
//

//찜한 도서들 이미지 가져오는 함수
$(function(){
        var userId= $('#my-info>div>a').text()

        $.ajax({
            url: "/mysite/mysite_wishlistbook",
            data: {'user_id': userId},
            success: function (data) {

                wishBookImgStr="<h2>찜한 책</h2>"
                str = ''

                data=data['books']


                for(var i =0;i<5;i++){

                    wishBookImgStr += "<div class='book-img-container' id='mysite-wishlist'"+i+">"
                    wishBookImgStr += "<img class='book-img'  src=" + data[i].cover_large + " name=" + data[i].book_id+ ">"
                    wishBookImgStr += "</div>"
                    $(".wish-img-container").html(wishBookImgStr);

                    // 더보기 버튼 새로 추가:
                    wishBookFullButton = '<div class="full-btn"><span class="btn" id="mysite-wishlist-btn"><a href="/mysite/all_wish">더보기</a></span></div>'
                    $(".wish-img-container").append(wishBookFullButton)
                }


            }
        })

    })

//유저의 이용현황 가져오는 함수
$(function(){
        var userId= $('#my-info>div>a').text()

        $.ajax({
            url: "/mysite/usage",
            data: {'user_id': userId},
            success: function (data) {
                var usageStr = ''
                var like_count = data['like']
                var dislike_count = data['dislike']
                var total_count = data['total']
                var wishlist_count = data['like']
                var history_count = data['like']
                like_percent = Math.round(like_count/total_count*100)
                dislike_percent = 100 - Math.round(like_count/total_count*100)
                usageStr += '<label>평가한 도서 수는? </label><br><span class=user-usage >'+total_count+'권</span><br>'
                usageStr += '<label>찜한 도서수 수는? </label><br><span class=user-usage >'+wishlist_count+'권</span><br>'
                usageStr += '<label>읽은 총 도서 수는? </label><br><span class=user-usage >'+history_count+'권</span><br>'
                usageStr += '<label>평가한 도서의 좋아요/싫어요 비율은?</label><br><span class=user-usage>'+like_percent+'%/'+dislike_percent+'%</span><br>'
                usageStr += "<div style='display: inline-block; width:200px; height:20px; background:white; border: 1px solid black; border-radius: 50px;'><div style='width: "+like_percent+"%; border-radius: 10px 0px 0px 10px; height: 20px; display: inline-block; background-color: lightblue';></div><div style='width:" + dislike_percent + "%; height: 20px; display: inline-block; border-radius: 0px 10px 10px 0px; background: lightpink';></div>"
                // 당신은 엄격파, 후한파, 적당파
                if (like_percent > 70){
                    var evaluation = "당신은 후한 점수를 주는 편입니다."
                } else if (like_percent < 30){
                    var evaluation="당신은 엄격한 편이시군요"
                } else{
                    var evaluation="당신은 다른 사람들과 비슷한 점수를 주는 편입니다."}
                usageStr += "<p class='evaluation_quote'>"+evaluation +"</p>"
                $(".usage").html(usageStr);

            }
        })

    })

//유저의 프로필 가져오는 함수
$(function(){
    var userId= $('#my-info>div>a').text()
    $.ajax({
        url: "/mysite/user_info",
        data: {'user_id': userId},
        success: function (data) {
            var userStr = ''
            var id = data['user_id']
            var email = data['user_email']

            var gender = data['gender']
            var nickname = data['nickname']
            var birth = data['birth']

            userStr += '<label>USERNAME: </label><span class=user-info-id ><input type="text" value="'+id+'" readonly></span><br>'
            userStr += '<label>E-MAIL: </label><span class=user-info id="user-info-email"><input type="text" value="'+email+'" readonly></span><br>'
            userStr += '<label>GENDER: </label><span class=user-info id="user-info-gender"><input type="text" value="'+gender+'" readonly></span><br>'
            userStr += '<label>NICKNAME: </label><span class=user-info-nickname><input type="text" value="'+nickname+'" readonly></span><br>'
            userStr += '<label>DATE OF BIRTH: </label><span class=user-info id="user-info-birth"><input type="date" value="'+birth+'" readonly></span><br>'
//            userStr += "<button id='update-info' onclick='updateInfo()'>수정</button>"

            $(".info").html(userStr);

        }
    })
})


// 유저프로필에서 수정버튼 눌렀을 때 동작
function updateInfo(){
//    var classname = '.user-info'.toString()

    if ($('.user-info>input').attr('readonly')){

        $('.user-info>input').attr('readonly',false)
        $('#update-info').html('저장')

    }else{
        //저장
        var user_id = $(".card>h1").text()
        var email = $('#user-info-email>input').val()
        var gender = $('#user-info-gender>input').val()
        var birth = $('#user-info-birth>input').val()

        $.ajax({
            url: "/mysite/mysite_update",
            data: {'user_id': user_id , 'email':email, 'gender':gender,'birth':birth},
            type: 'GET',
            success: function (data) {

            }
        })
        $('.user-info>input').attr('readonly',true)
        $('#update-info').html('수정')
    }
}

// 유저의 리뷰게시판 이용 내역 가져오는 함수
$(function(){
    var userId= $('#my-info>div>a').text()

        $.ajax({
            url: "/mysite/board",
            data: {'user_id': userId},
            success: function (data) {
                data=data['board']
                var boardStr = ''

                for(var i=0;i<data.length;i++){
                    boardStr += '<tr>'
                    boardStr += '<td>'+data[i].title+'</td>'
                    boardStr += '<td>'+data[i].board_content+'</td>'
                    boardStr += '<td>'+data[i].pubdate+'</td>'
                    boardStr += '</tr>'
                    $(".board-container").html(boardStr);
                }

            }
        })

    })

