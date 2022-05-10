from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.utils import timezone
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    user_id = request.session.get('user_id')


    board = Board.objects.all().order_by('-board_id')

    paginator = Paginator(board, 10)  # 한 페이지당 몇 개를 보여줄건지 지정

    page_num = request.GET.get('page', '1')  # 현재페이지 만약없으면 1
    page_obj = paginator.get_page(page_num)

    try:
        print(page_obj.next_page_number())  # page_obj.next_page_number() : 현재페이지에서 다음 페이지의 넘버 : 3
        print(page_obj.previous_page_number())  # page_obj.previous_page_number() : 현재 페이지에서 이전 페이지의 넘버 : 1
    except:
        pass

    return render(request, 'board/index.html', {'list': page_obj, 'user_id':user_id,'cnt':page_num})  # order_by('id')에서 id면 오름차순 -id면 내림차순


def detail(request,board_id):  #user_id값을 가지고 요청
    user_id = request.session.get('user_id')


    data = Board.objects.get(board_id=board_id)

    return render(request, 'board/detail.html',{'dto':data,'user_id':user_id})
    # 요청들어오면 detail.html반환하는데 Board의 객체들 중 user_id와 같은 객체를 찾아 db에 get방식으로 요청

def insert_form(request):
    user_id = request.session.get('user_id')

    data = {'user_id': user_id}
    return render(request, 'board/insert.html',data)

def insert_res(request):
    user_id = request.session.get('user_id') #post로 요청받은 myname의 벨류값을 myname변수에 저장
    book_id = request.POST.get('book_id')

    mycontent = request.POST['mycontent']
    mytitle = Book.objects.filter(book_id=book_id).values('title')[0]['title']


    result = Board.objects.create(
         book_id = book_id,
         user_id=user_id,
         board_content =mycontent,
         pubdate =timezone.now(),
         title = mytitle).save()
    #create 함수를 이용해 result 객체 생성, myname=myname , mytitle=mytitle... -> 각 요소값을 넣어줌


    return redirect('/board')


def update(request, board_id):

    result_content = request.POST.get('board-content')
    result_update = Board.objects.get(board_id=board_id)
    result_update.board_content=result_content
    result_update.save()

    return redirect('/board/detail/'+str(board_id))


def delete(request, board_id):
    result_delete = Board.objects.filter(board_id=board_id).delete()
    # result_delete = MyBoard.objects.filter(id=id).delete() 한 결과는 튜플로 나옴
    # id가 id인 애를 filter로 가져와서 삭제
    #print(result_delete) -> 결과: (1, {'myboard.MyBoard': 1})

    if result_delete[0]:  #result_delete의 반환값은 튜플인데 거기서 0번쨰 인덱스의 값이 있으면
        return redirect('index')
    else:
        return  redirect('detail/'+board_id)


# 독서노트 이미지 가져오는 곳
def booknote(request):

    user_id = request.session.get('user_id')
    book_id = request.GET.get('bookId')


    book_cover = Book.objects.filter(book_id=book_id).values('cover','book_id','title')[0]

    return JsonResponse(book_cover)

def booknote_search(request,book_id):
    user_id = request.session.get('user_id')
    book_id = book_id

    data = {'user_id': user_id,'book_id': book_id}

    return render(request, 'board/insert.html',data)
