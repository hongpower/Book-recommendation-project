$(function(){
    $('.btn-id-chk').click(function(){
         $('.id-check-container').empty()
        var username = $("input[name='username']").val()

        $.ajax({
            url: "/login/id_chk",
            data: {'user_id': username},
            success: function (data) {

                data=data['result']

                var checkStr=''


                checkStr +=   data

                $('.id-check-container').html(checkStr);


            }
        })
    })
})

$(function(){
    $('.btn-nickname-chk').click(function(){
         $('.nickname-check-container').empty()
        var nickname = $("input[name='nickname']").val()

        $.ajax({
            url: "/login/nickname_chk",
            data: {'nickname': nickname},
            success: function (data) {

                data=data['result']

                var checkStr=''


                checkStr +=   data

                $('.nickname-check-container').html(checkStr);


            }
        })
    })
})


$(function(){
    $("input[name='password']").on("change keyup paste",function(){
         $('.password-check-container').empty()
        var password = $("input[name='password']").val()

        $.ajax({
            url: "/login/password_chk",
            data: {'password': password},
            success: function (data) {

                data=data['result']

                var checkStr=''


                checkStr +=   data

                $('.password-check-container').html(checkStr);


            }
        })
    })
})