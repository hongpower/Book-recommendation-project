//좋아요 한 도서들 이미지 가져오는 함수
$(function(){

        $(".like-img-aricle").empty()
        var user_id = $(".card>h1").text()

        $.ajax({
            url: "/mysite/mysite_likebook",
            data: {'user_id': user_id},
            success: function (data) {

                likeBookImgStr=''
                str = ''

                data=data['books']
                for(var i =0;i<6;i++){
                        likeBookImgStr += "<div class='book-img-container' id='mysite-like'"+i+">"
                        likeBookImgStr += "<img class='book-img'  src=" + data[i].cover_large + " name=" + data[i].book_id+ ">"
                        likeBookImgStr += "</div>"
                }


                $(".like-img-aricle").html(likeBookImgStr);
            }
        })

    })
//

//찜한 도서들 이미지 가져오는 함수
$(function(){


        var user_id = $(".card>h1").text()

        $.ajax({
            url: "/mysite/mysite_wishlistbook",
            data: {'user_id': user_id},
            success: function (data) {

                wishBookImgStr=''
                str = ''

                data=data['books']


                for(var i =0;i<6;i++){
                    wishBookImgStr += "<div class='book-img-container' id='mysite-wishlist'"+i+">"
                    wishBookImgStr += "<img class='book-img'  src=" + data[i].cover_large + " name=" + data[i].book_id+ ">"
                    wishBookImgStr += "</div>"
                    $(".wish-img-article").html(wishBookImgStr);
                }


            }
        })

    })
//유저의 이용현황 가져오는 함수
$(function(){


        var user_id = $(".card>h1").text()

        $.ajax({
            url: "/mysite/usage",
            data: {'user_id': user_id},
            success: function (data) {
                var usageStr = ''
                var like_count = data['like']
                var dislike_count = data['dislike']
                var total_count = data['total']
                var wishlist_count = data['like']
                var history_count = data['like']
                usageStr += '<label>평가한 도서 수</label><span class=user-usage >'+total_count+'개</span><br>'
                usageStr += '<label>찜한 도서수 수</label><span class=user-usage >'+wishlist_count+'개</span><br>'
                usageStr += '<label>읽은 도서 수</label><span class=user-usage >'+history_count+'개</span><br>'
                usageStr += '<label>평가 도서 좋아요/싫어요 비율</label><span class=user-usage >'+Math.round(like_count/total_count*100)+'%/'+Math.round(dislike_count/total_count*100)+'%</span><br>'

                $(".usage").html(usageStr);

            }
        })

    })

//유저의 프로필 가져오는 함수
$(function(){
    var user_id = $(".card>h1").text()
    $.ajax({
        url: "/mysite/user_info",
        data: {'user_id': user_id},
        success: function (data) {
            var userStr = ''
            var id = data['user_id']
            var email = data['user_email']

            var gender = data['gender']
            var nickname = data['nickname']
            var birth = data['birth']

            userStr += '<label>아이디</label><span class=user-info-id ><input type="text" value="'+id+'" readonly></span><br>'
            userStr += '<label>이메일</label><span class=user-info id="user-info-email"><input type="text" value="'+email+'" readonly></span><br>'
            userStr += '<label>성별</label><span class=user-info id="user-info-gender"><input type="text" value="'+gender+'" readonly></span><br>'
            userStr += '<label>닉네임</label><span class=user-info-nickname><input type="text" value="'+nickname+'" readonly></span><br>'
            userStr += '<label>생년월일</label><span class=user-info id="user-info-birth"><input type="date" value="'+birth+'" readonly></span><br>'
            userStr += "<button id='update-info' onclick='updateInfo()'>수정</button>"

            $(".info").html(userStr);

        }
    })
})


// 유저프로필에서 수정버튼 눌렀을 때 동작
function updateInfo(){


//    var classname = '.user-info'.toString()

    if ($('.user-info>input').attr('readonly')){
        //수정
        //alert("떳냐")
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


        var user_id = $(".card>h1").text()

        $.ajax({
            url: "/mysite/board",
            data: {'user_id': user_id},
            success: function (data) {
                data=data['board']
                var boardStr = ''
                console.log(data)

                for(var i=0;i<data.length;i++){
                    console.log(data[i],'지수')
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

