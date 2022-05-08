$(function(){

    var username= $('.card>h1').text()

    $.ajax({
        url: "/profile",
        data:{'user_id':username},
        dataType: 'json',
        success: function (data) {
            var bookStr=''
            var nickname=data['nickname']
            var email = data['user_email']
            var read_book=data['read_book']

            bookStr += '읽은 책 수:'+ read_book

            $('#nickname').html(nickname)
            $('#email').html(email)
            $('#read_book>a').html(bookStr)

        }
    })
})