$(function(){

        $('.book-img-container').empty()
        var username = $("input[name='read-user-id']").val()
        $.ajax({
            url: "/history_register/history",
            data: {'user_id': username},
            success: function (data) {
                readBookImgStr=''
                str = ''

                data=data['books']

                for(var i =0;i<data.length;i++){

                    readBookImgStr = "<img class='book-img'  src=" + data[i].cover + " name=" + data[i].book_id+ "width=100 height=100>"
                    str += '<tr>'
                    str += '<td>'+readBookImgStr+'</td>'
                    str +=  '<td>' + data[i].title +'</td>'
                    str +=  '<td><input class="modify'+i+'" id="score'+i+'" type="number" min="0" max="5" step="0.5" value="'+data[i].score+'"readonly></td>'
                    str +=  '<td><input class="modify'+i+'" id="start'+i+'" type="date" value="'+data[i].start_date+'" readonly></td>'
                    str +=  '<td><input class="modify'+i+'" id="end'+i+'" type="date" value="'+data[i].end_date+'" readonly></td>'
                    str +=  "<td><span class='btn' id='update-btn'><button id='update-toggle"+i+"' onclick='updateHistory("+i+","+data[i].book_id+")'>수정</button></span></td>"
                    str +=  "<td><span class='btn' id='delete-btn'><button id='delete-toggle"+i+"' onclick='deleteHistory("+i+","+data[i].book_id+")'>삭제</button></span></td>"
                    str += '</tr>'


                $('.table-container').html(str);

                }

            }
        })

    })
function updateHistory(index,bookId){

    //if $('.modify').
    var classname = '.modify'+index.toString()
    if ($(classname).attr('readonly')){
        //수정
        $(classname).attr('readonly',false)
        $('#update-toggle'+index).html('저장')

    }else{
        //저장
        var username = $("input[name='read-user-id']").val()
        var score = $('#score'+index).val()
        var start_date = $('#start'+index).val()
        var end_date = $('#end'+index).val()


        $.ajax({
            url: "/history_register/history_update",
            data: {'user_id': username , 'score':score, 'start_date':start_date,'end_date':end_date,'book_id':bookId},
            type: 'GET',
            success: function (data) {

            }
        })
        $(classname).attr('readonly',true)
        $('#update-toggle'+index).html('수정')
    }
}

function deleteHistory(index,bookId){
    var username = $("input[name='read-user-id']").val()

    var result= confirm("삭제하시겠습니까?")
    if(result){
        $.ajax({

        url:"/history_register/history_delete",
        data: {'user_id':username, 'book_id':bookId},
        type:'GET',
        success: function(data){

        }
    })



    createHistory()
    }else{

    }

}



function createHistory(){
    $('.book-img-container').empty()
        var username = $("input[name='read-user-id']").val()



        setTimeout(function(){
            $.ajax({
                url: "/history_register/history",
                data: {'user_id': username,'chk':'second'},
                success: function (data) {



                    readBookImgStr=''
                    str = ''

                    data=data['books']
                    if(data.length==0){
                        $('.book-img-container').empty();
                        $('.table-container').empty();
                    }else{
                        for(var i =0;i<data.length;i++){

                            readBookImgStr = "<img class='book-img'  src=" + data[i].cover + " name=" + data[i].book_id+ ">"
                            str += '<tr>'
                            str +=  '<td>' + readBookImgStr +'</td>'
                            str +=  '<td>' + data[i].title +'</td>'
                            str +=  '<td><input class="modify'+i+'" id="score'+i+'" type="number" min="0" max="5" step="0.5" value="'+data[i].score+'"readonly></td>'
                            str +=  '<td><input class="modify'+i+'" id="start'+i+'" type="date" value="'+data[i].start_date+'" readonly></td>'
                            str +=  '<td><input class="modify'+i+'" id="end'+i+'" type="date" value="'+data[i].end_date+'" readonly></td>'
                            str +=  "<td><span class='btn' id='update-btn'><button id='update-toggle"+i+"' onclick='updateHistory("+i+","+data[i].book_id+")'>수정</button></span></td>"
                            str +=  "<td><span class='btn' id='delete-btn'><button id='delete-toggle"+i+"' onclick='deleteHistory("+i+","+data[i].book_id+")'>삭제</button></span></td>"
                            str += '</tr>'




                        $('.table-container').html(str);

                        }
                    }
                }
            })},300)

}

