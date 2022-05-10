$(function(){
    new Swiper('.swiper-container', {
        // 방향: vertical 수직, horizontal 수평, default: horizontal
        direction: 'horizontal',
        // 드래그 기능 true/false
        debugger: false,
        // 무한 반복 기능 true/false
        loop: false,
        // 마지막 슬라이드 -> 첫슬라이드 자연스러운 반복 기능
        loopAdditionalSlides: 1,
         // 슬라이드 사이 여백
        spaceBetween : 0,
        // 한번에 보여 줄 슬라이드 개수
        slidesPerView: 1,
        // 그룹으로 묶을 슬라이드 수
        slidesPerGroup: 1,
        // 자동 스크롤링
        autoplay: {
            // 1000: 1초
            delay: 200000,
            // 여기 수정:
            disableOnInteraction: true,
        },
        // 페이징
        pagination: {
            // 페이징 클래스명
            el: '.swiper-pagination',
            // 클릭 가능 true/false
            clickable: true,
            // 타입: fraction, bullets, progressbar
            type: 'fraction',
        },
        // observer와 observeParents주기
        observer:true,
        observerParents:true,

        // 네비게이션
        navigation: {
            // 다음 버튼 클래스명
            nextEl: '.swiper-button-next',
            // 이전 버튼 클래스명
            prevEl: '.swiper-button-prev',
        },
    })
})