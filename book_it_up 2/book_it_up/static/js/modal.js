$(function(){
    // 책 이미지 클릭하면 모달창 열기 :
    $(".book-img-container").on("click", function(event){
        // 책 isbn와 imgUrl 가져오기
        const bookId = $(this).find("img").attr("name")
        const imgUrl = $(this).find("img").attr("src")
        console.log(bookId)
        console.log(imgUrl)

        // 1) 기존 내용 삭제하고 모달 창에 원하는 정보 넣기
        // $("#modal-content").html()
        $(".modal-content > div > div").html('')
        
        $.ajax({
            url: '/book_id/',
            data: {'bookId' : bookId},
            dataType: 'json',
            success: function(data){
                console.log(data)
                var topBoxInfo = data.all[0]
                var bottomBoxInfo = data.all[1]
                /*
                var title=data.title
                var isbn13=data.book_id
                var author=data.author
                var publisher=data.publisher
                var translator=data.translator
                var category=data.category
                var price=data.price
                var keywords=data.keywords
                var score=data.score
                var reviews=data.reviews
                var phrases=data.phrases
                
                */

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
                            
                        }
                        var info = "<li id=" + key + " class='info' >" + data[key] + "</li>"
                        $(".info-list").append(info)

                    }
                    
                
                for (key in bottomBoxInfo){
                    console.log(key)
                    if (key=="desc"){
                        $("#bottom-small-box").html("<div class='desc'></div>")
                        $(".desc").append('<div class="bottom-box-title">줄거리:</div>')
                        $(".desc").append("<p>" + bottomBoxInfo[key]+"</p>")

                    } 
                    
                    else if (key=="review"){
                        console.log("review시작")
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
            }
         
        })   

        // 2) 모달 창 보여주기
        $("#modal").show();
        // 3) 모달창을 제외한 body를 비활성화 시키는 backon 클래스 추가
        $("body").append("<div class='backon'></div>")
    })

    $("body").on("click", function(event){
        if(event.target.className == "close" || event.target.className == "backon"){
            $("#modal").hide();
            $(".backon").hide();
        }
    })

})