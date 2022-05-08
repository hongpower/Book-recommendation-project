$(function(){
// 책 이미지 hover 하면 button 넣기 :
$(".like-btn").on("click", function(){
    // 좋아요 했다는 class 를 넣고
    $(this).toggleClass('in_likes')

    // dislike가 있었으면 db에서 제외하기
    dislikeChk = $(this).parent().next().find('.btns').hasClass("in_dislikes")

    // dislike는 빼기
    $(this).parent().next().find('.btns').removeClass('in_dislikes')

    // 클래스 포함여부에 따라 좋아요인지 좋아하지 않아요인지 판단.
    likeChk = $(this).hasClass("in_likes")

    // bookId는 parent(span태그)의 book-img클래스의 name
    bookId = $(this).parent().parent().find('.book-img').prop('name')

    modifyPreference(bookId, likeChk, dislikeChk, 'like_btn')})

$(".dislike-btn").on("click", function(){
    $(this).toggleClass('in_dislikes')

    // like가 있었으면 db에서 제외하기
    likeChk = $(this).parent().prev().find('.btns').hasClass("in_likes")

    $(this).parent().prev().find('.btns').removeClass('in_likes')

    // 클래스 포함여부에 따라 좋아요인지 좋아하지 않아요인지 판단.
    dislikeChk = $(this).hasClass("in_dislikes")

    // bookId는 parent(span태그)의 book-img클래스의 name
    bookId = $(this).parent().parent().find('.book-img').prop('name')

    modifyPreference(bookId, likeChk, dislikeChk, 'dislike_btn')})

$(".wishlist-btn").on("click", function(){
    console.log('hihihihi')
    $(this).toggleClass('in_wishlist')

    // bookId는 parent(span태그)의 book-img클래스의 name
    bookId = $(this).parent().parent().find('.book-img').prop('name')

    wishlistChk = $(this).hasClass("in_wishlist")

    modifyWishlist(bookId, wishlistChk)})


    // 책 이미지 클릭하면 모달창 열기 :
    $(".book-img-container").on("click", function(event){
        // 좋아요/싫어요/찜하기 버튼이 아니라면 :
        console.log($(event.target).closest(".btns").length)
        if (!$(event.target).closest(".btns").length){
            console.log($(event.target).closest(".btns").length)
            // 책 isbn와 imgUrl 가져오기
            const bookId = $(this).find("img").attr("name")
            const imgUrl = $(this).find("img").attr("src")

            // 1) 기존 내용 삭제하고 모달 창에 원하는 정보 넣기
            $(".modal-content > div > div").html('')

            $.ajax({
                url: '/book_id/',
                data: {'bookId' : bookId},
                dataType: 'json',
                success: function(data){
                    // 만약 no_info라면 :
                    console.log(data.all)
                    console.log(data.all.length)
                    if (data.all.length <= 1){
                        alert("해당 책의 세부 정보가 없습니다.")
                    } else {
                        var topBoxInfo = data.all[0]
                        var bottomBoxInfo = data.all[1]

                        $("#left-box").html("<img src=" + imgUrl + ">")
                        $("#right-box").append("<ul class='info-list'></ul>")

                        for (key in topBoxInfo){
                            data = topBoxInfo
                            if (data[key] != null & data[key] != ""){
                                if (key=="title"){
                                    //title에 부가 제목 있으면 <br>넣기
                                    titleAry = data[key].split("-")
                                    data[key] = titleAry[0]
                                    var info = "<li id=" + key + " class='info' >" + data[key] + "</li>"
                                    $(".info-list").append(info)
                                    if (titleAry.length > 1){
                                        data['subtitle'] = titleAry[1]
                                        var info = "<li id=" + key + " class='info' >" + data['subtitle'] + "</li>"
                                        $(".info-list").append(info)
                                    }
                                    continue
                                }
                                if (key=="book_id"){
                                    data[key] = '(isbn13: '+ data[key] + ')'
                                }
                                if (key=="cover"){
                                    $("#left-box").html("<img src=" + data[key] + ">")
                                    continue
                                }

                                if (key=="pubdate"){
                                    data[key] = '출간일: ' + data[key]
                                }
                                if (key=="translator"){
                                    data[key] = data[key] + "(옮긴이)"
                                }

                                if (key=="publisher"){
                                    data[key] = "출판사: " + data[key]
                                }

                                if (key=="price"){
                                    // 콤마들어가는 정수형으로 바꾸고 원화 기호 넣기
                                    data[key] = parseInt(data[key])
                                    data[key] = "₩" + data[key].toLocaleString()
                                }
                                if (key=="score"){
                                    score = Math.floor(parseInt(data[key])/2)
                                    // 별점 그릴 div 태그 만들기 :
                                    $("#right-box").append("<div class='star-box'></div>")
                                    // 별 5개 그리기 :
                                    var star_str = "<span class='on-star'>★</span>"
                                    for (var i=0; i<score; i++){
                                        $(".star-box").append(star_str)
                                    }
                                    var star_str = "<span class='off-star'>★</span>"
                                    for (var i=0; i<(5-score); i++){
                                        $(".star-box").append(star_str)
                                    }
                                    continue
                                }
                                if (key=="keyword"){

                                    $("#right-box").append("<div id='keyword-box'></div>")
                                    $.each(data['keyword'], function(index, value){
                                        if ((index)%5 == 0 && (index) != 0){
                                            $("#keyword-box").append("<br><br>")
                                        }
                                        $("#keyword-box").append("<span>"+value+"</span>")
                                    })
                                    continue
                                    }

                                    var info = "<li id=" + key + " class='info' >" + data[key] + "</li>"
                                    $(".info-list").append(info)
                                }
                                //var info = "<li id=" + key + " class='info' >" + data[key] + "</li>"
                                //$(".info-list").append(info)




                        for (key in bottomBoxInfo){
                            if (key=="desc"){
                                $("#bottom-small-box").html("<div class='desc'></div>")
                                $(".desc").append('<div class="bottom-box-title">줄거리:</div>')
                                $(".desc").append("<p>" + bottomBoxInfo[key]+"</p>")

                            }

                            else if (key=="review"){
                                $("#bottom-small-box").append("<div class='reviews'></div>")
                                $('.reviews').append("<ul id='reviewAry'></ul>")
                                $('#reviewAry').append("<li class='bottom-box-title'>리뷰:</li>")
                                console.log(bottomBoxInfo[key])
                                $.each(bottomBoxInfo[key][0], function(index, value){
                                    $("#reviewAry").append("<li>"+value+"</li>")
                                })
                            }


                             else if (key=="phrase"){
                                $("#bottom-small-box").append("<div class='phrase'></div>")
                                $('.phrase').append("<ul id='phraseAry'></ul>")
                                $('#phraseAry').append("<li class='bottom-box-title'>대사:</li>")
                                console.log(bottomBoxInfo[key])
                                $.each(bottomBoxInfo[key][0], function(index, value){
                                    $("#phraseAry").append("<li>"+value+"</li>")
                                })
                            }

                        }
                                // 2) 모달 창 보여주기
                        $("#modal").show();
                        // 3) 모달창을 제외한 body를 비활성화 시키는 backon 클래스 추가
                        $("body").append("<div class='backon'></div>")

                         $("body").on("click", function(event){
                            if(event.target.className == "close" || event.target.className == "backon"){
                                $("#modal").hide();
                                $(".backon").hide();
                            }
                        })

                    }
                }
                }

            })

        }

    })

})



// db에 선호도 정보를 저장하는
function modifyPreference(bookId, likeChk, dislikeChk, triggeredBtn){
    $.ajax({
        url: '/modify_preference',
        data: {'book_id': bookId, 'like_chk': likeChk, 'dislike_chk': dislikeChk, 'triggered_btn': triggeredBtn},
        success: function(data){
            if(data=="fail"){
                console.log(data)
                alert('해당 책은 선호도 등록이 불가능합니다.')
                $("img[name='"+bookId+"']").next().next().find('.btns').removeClass('in_likes')
                $("img[name='"+bookId+"']").next().next().next().find('.btns').removeClass('in_dislikes')
            }
        }

    })
}

function modifyWishlist(bookId, wishlistChk){
    $.ajax({
        url: '/modify_wishlist',
        data: {'book_id': bookId, 'wishlist_chk': wishlistChk},
        success: function(data){
            if(data=="fail"){
                alert('해당 책은 찜기능을 제공하지 않습니다.')
                $("img[name='"+bookId+"']").next().find('.btns').removeClass('in_wishlist')
            }
        }

    })
}
