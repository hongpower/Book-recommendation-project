$(function(){

    var $nav = $("nav")
    var $page = $('.page-start')
    var $window = $(window)
    var pageOffsetTop = $page.offset().top
    var userId= $('#my-info>div>a').text()

    // nav바 오른쪽 my-info 생성
    $.ajax({
        url: "/profile",
        data:{'user_id':userId},
        dataType: 'json',
        success: function (data) {
            var bookStr=''
            var nickname=data['nickname']
            var email = data['user_email']
            var read_book=data['read_book']

            bookStr += '읽은 책 수: '+ read_book +'권'

            //$('#nickname').html(nickname)
            //$('#email').html(email)
            $('#read_book>a').html(bookStr)

        }
    })
    // window사이즈가 resize 되면 top 값 다시 계산하기 :
    $window.resize(function(){
        pageOffsetTop = $page.offset().top;
    })

    $window.on("scroll", function(){
        var scrolled = $window.scrollTop() >= pageOffsetTop; //스크롤 한 위치가 window size보다 크다면 
        console.log(pageOffsetTop)
        $nav.toggleClass("down", scrolled)
    })

    var $page = $("nav > ul > li > a")
    $page.on("mouseenter", function(){
        $(this).prop("class", "on-page")
    })
    $page.on("mouseleave", function(){
        $(this).removeClass("on-page")
    })

    $(".next").click(function(){
        $("#")
    })

    new Swiper('.swiper-container', {
        direction: 'horizontal',
    })
    $(".parent-menu > a").click(function(){
        var submenu=$(this).parent().next("ul");

        // 클릭된 메뉴에서 class가 menu인 li태그 선택 :
        var menuContainer=$(this).parent().parent()
        if (submenu.is(":visible")){
            submenu.slideUp();
            // 메뉴가 슬라이드 끝까지 슬라이드 업되고 메뉴가 사라지게 하기 위해서 딜레이 :
            setTimeout(function(){
               menuContainer.removeClass("full-menu")
            }, 200)
        } else {
            submenu.slideDown();
            setTimeout(function(){
                menuContainer.prop("class", "full-menu")
            }, 200)
        }
    })

    // 로그인이 돼있지 않다면:
    var user_id = "{{ request.session.user_id }}"
    
    GetUserId()

})
function GetUserId(){
    var user_id = '<%= Session["user_id"] %>'
}

$(function(){


})

$(function(){
    $.ajax({
        url:'/bestbook/',
        success:function(data){
            bookRank=''

            data=data['books']

            for(var i =0;i<10;i++){ // 상위 몇개 가져올지만 정하면 됨 -> 상위 10개만

                bookRank += '<tr>'
                bookRank += '<td>'+(i+1)+'</td>'
                bookRank += '<td>'+data[i].title+'</td>'
                bookRank += '<td>'+data[i].score_avg+'</td>'
                bookRank += '<td>'+data[i].history_cnt+'</td>'
                bookRank += '</tr>'

            }


            $(".rank-book").html(bookRank);
        }
    })
})
