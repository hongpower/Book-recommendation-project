$(function(){
    var $nav = $("nav")
    var $page = $('.page-start')
    var $window = $(window)
    var pageOffsetTop = $page.offset().top
    
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
    $(".menu>a").click(function(){
        var submenu=$(this).next("ul");
        if(submenu.is(":visible")){
            submenu.slideUp();
        }
        else{
            submenu.slideDown();
        }
    })

    // 로그인이 돼있지 않다면:
    var user_id = "{{ request.session.user_id }}"
    
    GetUserId()
})
function GetUserId(){
    var user_id = '<%= Session["user_id"] %>'
}


