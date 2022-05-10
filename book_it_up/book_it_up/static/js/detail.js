$(function(){
    var userId= $('#my-info>div>a').text()
    var writer= $('#writer').val()

    
    var res = (userId==writer)
    if(res==true){
        $('#update-toggle').attr('disabled',false)
        $('#delete-toggle').attr('disabled',false)
    }else{
        $('#update-toggle').attr('disabled',true)
        $('#update-toggle').attr('type','hidden')
        $('#delete-toggle').attr('disabled',true)
        $('#delete-toggle').attr('type','hidden')
    }

})

function contentUpdate(){

    if($('#board-content').attr('readonly')){
        $('#board-content').attr('readonly',false)
        $('#update-toggle').attr('value','저장')
    }else{
        $('#board-content').attr('readonly',true)
        $('#update-toggle').attr('value','수정')

        $('#update-form').submit()

    }
}

