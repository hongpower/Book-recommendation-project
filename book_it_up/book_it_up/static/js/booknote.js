$(function(){

        var userId= $('#my-info>div>a').text()
        var bookId= $('#book-id').val()
        $.ajax({
            url: "/board/book_note/",
            data : {'bookId':bookId},
            dataType: 'json',
            success: function (data) {

                var bookImageStr=''

                var bookId=data.book_id
                var cover=data.cover
                console.log(bookId)
                bookImageStr += "<img class='book-img' src=" + cover + " name=" + bookId+ ">"


                $('.book-img-container').html(bookImageStr);
                $("#book_id").val(bookId);
            }
        })

    })