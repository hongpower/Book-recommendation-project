from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import random
from pymongo import MongoClient
from django.contrib import messages
import json
from .secrets import mongo_user, mongo_pw, ip_address, port_num
from datetime import datetime
from django.utils import timezone
from datetime import datetime
from django.db.models import Avg
from haystack.views import SearchView

from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet

client = MongoClient("mongodb://" + mongo_user + ":" + mongo_pw + "@" + ip_address + ":" + port_num)


def index(request):

    user_id = request.session.get('user_id')


    # 1) 처음 가입하거나 아직 10개 이상의 좋아요를 하지 않은 유저라면 test 페이지로 보내기:
    user_history_logs = len(LikeTab.objects.filter(user_id=user_id))
    # if (user_id !=None) & (user_history_logs <= 10):
    #     return render(request, 'book_it_up/index.html', {'user' : 'first_user'})

    no_of_love_books = 20
    no_of_timely_books = 20
    no_of_short_books = 20

    final_lst = list()
    final_dict = dict()

    # 짧은 책 랜덤으로 불러오기, page수 150이하, 무게 150이하, 높이 150이하, 가로길이 150이하로 0/null 아닌 값  :
    books = BookSize.objects.filter(width__lte=200, height__lte=200, weight__lte=300, weight__gte=200)

    book_lst = []
    for i in range(len(books)):
        rand_n=random.randint(0, len(books)-1)
        book_lst.append(books[rand_n].book_id)

    books = BookGrade.objects.filter(book_id__in=book_lst).order_by('-score')

    for i in range(len(book_lst)):
        rand_n=random.randint(0, len(books)-1)
        book_lst.append(books[rand_n].book_id)

    books = BookCover.objects.filter(book_id__in=book_lst)

    rand_n = random.sample(range(len(books)), no_of_short_books)

    for i in range(0, no_of_short_books, 5):
        five_books_lst = list()
        for j in rand_n[i:i+5]:
            book = books[j]
            temp = dict()
            temp['book_id'] = book.book_id
            temp['img_url'] = book.cover_large
            five_books_lst.append(temp)

        final_lst.append(five_books_lst)

    final_dict['short_books'] = final_lst

    if user_id:
        final_dict['user_id']=user_id

    # 낮/밤별로 읽기 좋은 책 추천하기
    # 1) 시간대 가져오기

    db = client.book
    collection = db.keyword

    night_keywords = ['인생', '위로', '내면', '인간관계', '감정', '상처', '마음', '일상', '공감', '사람', '삶', '관계', '치유', '감성에세이', '대화', '외로움', '고독', '우정', '미움', '삶의지혜', '아픔', '친구', '그리움', '심리', '추억', '철학자', '고민', '철학', '우울증', '사색', '사유', '힐링', '생각', '일기', '감성', '감동', '어른을위한동화', '감성', '에세이', '글귀', '심리상담', '일기장', '풍자', '새벽', '휴식', '눈물', '심리치유', '속', '마음', '격려', '다이어리', '인생', '수업', '마음치유', '마음속', '마음챙김', '마음', '공부', '불면증', '심리', '치료', '심리', '치료사', '불면', '평온', '감사', '일기']
    morning_keywords = ['자기관리', '자신', '커리어', '성공', '멘토', '스펙', '청춘', '자기혁신', '재테크', '성장', '성공법', '리더십', '용기', '리더', '조언', '지혜', '처세', '명상', '인생처세술', '자기계발', '희망', '성장소설', '변화', '긍정', '인사이트', '소통', '자존감', '성공스토리', '성찰', '성공학', '직장처세술', '성장', '소설', '멘탈', '청춘', '소설', '시간관리', '멘토링', '도전', '통찰', '노력', '실행력', '성공', '법칙', '꿈', '목표', '달성', '젊음', '버킷', '리스트', '마인드컨트롤', '에너지', '성과', '창의성', '시간', '관리', '효능감', '진로', '실천', '몰입', '웃음', '열정', '명언', '명상에세이', '집중', '집중력', '동기부여', '잠재력', '성숙', '자신감', '인생론', '존재감', '평안', '평화', '업무력', '계획', '체력', '목표달성', '창의력', '자아존중감', '터닝', '포인트', '스트레칭', '성취', '시간', '관리법']
    love_keywords = ['사랑', '행복', '시집', '연애', '로맨스', '이별', '로맨스소설', '연애소설', '편지', '연인', '운명', '사랑 이야기', '첫사랑', '커플', '인연', '애인', '한국로맨스소설', '봄밤', '짝사랑', '고백', '낭만', '연애편지', '남자 친구', '여자 친구', '떨림', '실연', '연애담', '남녀 관계', '러브 스토리', '연애 세포', '프러포즈', '연애에세이', '청혼', '남녀', '연인 관계', '키스', '소개팅', '재밌는', '베스트셀러', '밀리언셀러', '노벨문학상', '퓰리처상', '노벨 문학상', '스테디셀러', '아마존 베스트셀러']

    # 2) 밤인지 낮인지 확인 후 해당 키워드 3개 이상 가진 책으로 추천
    isbn_lst = list()
    keyword_book_isbn = collection.find()
    
    hour_now = datetime.now().hour
    print('현재시간은', hour_now)
    if 4 <= hour_now <= 16:
        final_dict['is_daytime'] = True
        keyword_list = morning_keywords

    else:
        final_dict['is_daytime'] = False
        keyword_list = night_keywords

    # 책 한 권마다 모든 키워드 확인
    for book in keyword_book_isbn:
        temp_dict = {}

        temp_keyword_lst = book['keyword']

        for keyword in temp_keyword_lst:

            if keyword in keyword_list:
                isbn_lst.append(book['isbn13'])

    final_keyword_isbn_lst = list()
    for isbn in isbn_lst:
        if isbn_lst.count(isbn) > 3:
            final_keyword_isbn_lst.append(isbn)


    # 3) 해당 isbn으로 책 정보 가져오기
    hourly_books = BookCover.objects.filter(book_id__in=final_keyword_isbn_lst)

    hourly_book_list = list()

    # 중복없는 숫자로 :
    rand_n = random.sample(range(len(hourly_books)), no_of_timely_books)

    for i in range(0,no_of_timely_books, 5):
        five_books_lst = list()
        for j in rand_n[i:i + 5]:
            book = hourly_books[j]
            temp = dict()
            temp['book_id'] = book.book_id
            temp['img_url'] = book.cover_large
            five_books_lst.append(temp)

        hourly_book_list.append(five_books_lst)
    final_dict['hourly_books'] = hourly_book_list


    ## 연애 관련 도서 추천
    keyword_book_isbn = collection.find()
    keyword_list = love_keywords
    isbn_lst = list()

    for book in keyword_book_isbn:
        temp_keyword_lst = book['keyword']

        for keyword in temp_keyword_lst:

            if keyword in keyword_list:
                isbn_lst.append(book['isbn13'])

    final_keyword_isbn_lst = list()

    for isbn in isbn_lst:
        if isbn_lst.count(isbn) > 3:
            final_keyword_isbn_lst.append(isbn)

    # 3) user 정보가 없거나 19세 이하일 때는 성인물 금지:
    try:
        user_birth = User.objects.filter(user_id=user_id)[0].birth
        if user_birth.year > 2002 :
            user_identity = "underage"
        else :
            user_identity="adult"

    except:
        user_identity = "unknown"

    # 4) 해당 isbn으로 책 정보 가져오기
    if (user_identity == "underage") | (user_identity=="unknown"):
        filtered_books = Book.objects.filter(book_id__in=final_keyword_isbn_lst).filter(adult=False)
        filtered_book_isbn = [bk.book_id for bk in filtered_books]
        love_books = BookCover.objects.filter(book_id__in=filtered_book_isbn)
    else:
        love_books = BookCover.objects.filter(book_id__in=final_keyword_isbn_lst)

    love_book_list = list()

    # 중복없는 숫자로 :

    rand_n = random.sample(range(len(love_books)), no_of_love_books)

    for i in range(0, no_of_love_books, 5):
        five_books_lst = list()
        for j in rand_n[i:i+5]:
            book = love_books[j]
            temp = dict()
            temp['book_id'] = book.book_id
            temp['img_url'] = book.cover_large
            five_books_lst.append(temp)
        love_book_list.append(five_books_lst)

    final_dict['love_books'] = love_book_list

    return render(request, 'book_it_up/index.html', final_dict)

# 로그인 안한 상태에서 다른 페이지 이동하려고 할 때 :
def unlogged(request):
    return render(request, 'book_it_up/unlogged.html')

# 책 정보 가져오는 함수 :
def get_info(request):
    book_id = request.GET['bookId']

    # 해당 책이 추천 책이 아니라 전체 책이라면:

    try:
        desc = BookDesc.objects.filter(book_id=book_id).values("description1")[0]['description1']
        print(desc)
    except:
        print('정보없음')
        no_info = dict()
        no_info['all'] = [{'book_id' : "no_info"}]
        return JsonResponse(no_info)

    """
    book = BookDesc.objects.filter(book_id=book_id).values()
    if len(book) < 2:
        print('정보없음')
        no_info = {'book_id' : "no_info"}
        return JsonResponse(no_info)
    """

    # 기본 정보
    all_book_info = Book.objects.filter(book_id=book_id).values()[0]

    top_box_info = dict()
    top_box_info['title'] = all_book_info['title']
    top_box_info['book_id'] = all_book_info['book_id']
    top_box_info['author'] = all_book_info['author']
    top_box_info['translator'] = all_book_info['translator']
    top_box_info['publisher'] = all_book_info['publisher']
    top_box_info['pubdate'] = all_book_info['pubdate']
    top_box_info['price'] = all_book_info['price']
    top_box_info['category'] = all_book_info['category']

    # 점수
    score = BookGrade.objects.filter(book_id=book_id).values("score")[0]['score']
    top_box_info['score'] = score

    # 표지
    cover = BookCover.objects.filter(book_id=book_id).values("cover_large")[0]['cover_large']
    top_box_info['cover'] = cover

    # 키워드(mongo)
    db = client.book
    collection = db.keyword
    keywords = collection.find({'isbn13': book_id})[0]['keyword']
    keyword_lst = list()
    for keyword in keywords:
        keyword_lst.append(keyword)
    top_box_info['keyword'] = keyword_lst
    
    # ========================
    
    bottom_box_info = dict()    
    
    # 줄거리
    # desc는 정보있는지 없는지 확인용도로 이미 불러옴
    #desc = BookDesc.objects.filter(book_id=book_id).values("description1")[0]['description1']
    bottom_box_info['desc'] = desc
    
    # 리뷰(mongo)
    collection = db.review
    reviews = collection.find({'book_id': book_id})

    review_lst = list()
    for review in reviews:
        review_lst.append(review['review'])
    bottom_box_info['review'] = review_lst

    # phrase
    phrase_lst = list()
    phrases = Phrase.objects.filter(book_id=book_id).values("phrase_content")
    for phrase in phrases:
        phrase['phrase_content'].replace("  ", "")
        phrase_lst.append(phrase['phrase_content'])
    bottom_box_info['phrase'] = [phrase_lst]

    total_box_info = dict()
    total_box_info['all'] = [top_box_info, bottom_box_info]
    return JsonResponse(total_box_info)

# 사용자 선호도 정보를 db에 저장하는 구문:
def modify_preference(request):
    user_id = request.session.get('user_id')
    book_id = request.GET.get('book_id')

    # 해당 책이 등록됐는지 확인하기 위함 :
    try:
        desc = BookDesc.objects.filter(book_id=book_id).values("description1")[0]['description1']
    except:
        return HttpResponse ('fail')

    # 문자열로 받기 때문에 boolean으로 변경하기 :
    dislike_chk = json.loads(request.GET.get('dislike_chk'))
    like_chk = json.loads(request.GET.get('like_chk'))

    # 해당 함수를 호출한 버튼(좋아요/싫어요) 확인
    triggered_btn = request.GET.get('triggered_btn')

    if (like_chk) & (triggered_btn == 'like_btn'):
        like = LikeTab.objects.create(
            like_id='L' + user_id + book_id + 'd',
            user_id=user_id,
            book_id=book_id
        )
        like.save()

        # 만약 dislike가 기존에 돼있었따면 삭제:
        if dislike_chk:
            dislike = DislikeTab.objects.filter(user_id=user_id, book_id=book_id)
            dislike.delete()

    elif (dislike_chk) & (triggered_btn == 'dislike_btn'):
        dislike = DislikeTab.objects.create(
            dislike_id='D' + user_id + book_id + 'e',
            user_id=user_id,
            book_id=book_id
        )
        dislike.save()

        if like_chk:
            like = LikeTab.objects.filter(user_id=user_id, book_id=book_id)
            like.delete()

    # 만약 unlike만 했다면 삭제만 한다:
    elif ((triggered_btn) == 'like_btn') & (like_chk == False):
        LikeTab.objects.filter(user_id=user_id, book_id=book_id).delete()

    # 만약 undislike만 했다면 삭제만 한다:
    elif ((triggered_btn) == 'dislike_btn') & (dislike_chk == False):
        DislikeTab.objects.filter(user_id=user_id, book_id=book_id).delete()

    return HttpResponse('success')

def modify_wishlist(request):
    user_id = request.session.get('user_id')
    book_id = request.GET.get('book_id')

    # 해당 책이 등록됐는지 확인하기 위함 :
    try:
        desc = BookDesc.objects.filter(book_id=book_id).values("description1")[0]['description1']
    except:
        return HttpResponse ('fail')

    wishlist_chk = json.loads(request.GET.get('wishlist_chk'))

    if wishlist_chk:
        # append to wishlist
        wishlist = Wishlist.objects.create(
            book_id = book_id,
            user_id = user_id,
            wishlist_id = book_id + user_id + "3"
        )
        wishlist.save()

    else:
        # remove from wishlist
        Wishlist.objects.filter(book_id=book_id, user_id=user_id).delete()

    return HttpResponse('success')

# about_us 페이지
def get_about_us(request):
    user_id = request.session.get('user_id')
    return render(request, 'book_it_up/about_us.html', {'user_id': user_id})


# 내정보 확인하는 페이지 연결해주는 함수 :
def mysite(request):
    user_id = request.session.get('user_id')
    data={'user_id':user_id}
    return render(request,'book_it_up/mysite.html',data)

def book_photo(request):
    list1 = []
    for i in range(1, 11):
        num = random.randint(0, 233862)
        list1.append(num)

    dic_data = []
    book_info = Book.objects.values('book_id', 'cover')
    for j in list1:
        data = book_info[j]
        dic_data.append(data)
    json_data = {'books': dic_data}

    return JsonResponse(json_data)

# preference.html 연결해주는 함수 :
def get_preference(request):
    user_id=request.GET['user_id']
    data={'user_id':user_id}
    return render(request, 'book_it_up/test.html',data)

# Test 페이지용 책 가져오는 함수 :
def get_book(request):
    user_id = request.session.get('user_id')
    print(user_id)

    # 사용자가 기존에 평가 내렸던 책은 제외하기

    like_books = list(LikeTab.objects.values().filter(user_id=user_id).values('book_id'))
    dislike_books = list(DislikeTab.objects.values().filter(user_id=user_id).values('book_id'))
    wishlist_books = list(Wishlist.objects.values().filter(user_id=user_id).values('book_id'))
    eval_done_book_list = like_books + dislike_books + wishlist_books
    eval_done_book_isbn_lst = [x['book_id'] for x in eval_done_book_list]
    book_info = BookCover.objects.values('book_id', 'cover_large').exclude(book_id__in=eval_done_book_isbn_lst)

    # 랜덤으로 책 뽑기 :
    num = random.randint(0, len(book_info))
    lst_data= []
    data = book_info[num]
    lst_data.append(data)
    json_data = {'books': lst_data}

    return JsonResponse(json_data)

def search(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    # ajax 요청이라면 :
    if is_ajax:
        print('하이하이하이')
        sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
        #sqs = SearchQuerySet().filter(content_auto=request.GET.get('q', ''))

        suggestions = [result.title for result in sqs]

        context = {'results' : suggestions}

        return JsonResponse(context, safe=False)

    request.GET.get('')

    user_id = request.session.get('user_id')
    if user_id:
        final_dict = {}
        final_dict['user_id']=user_id
        return render(request, 'search/search.html', final_dict)

    else:
        return render(request, 'search/search.html')

# 자동완성 기능 추가:
def auto_complete(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    # ajax 요청이라면 :
    if is_ajax:
        sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
        suggestions = [result.title for result in sqs]

        context = {'results' : suggestions}

        return JsonResponse(context, safe=False)

    user_id = request.session.get('user_id')

    if user_id:
        final_dict = {}
        final_dict['user_id'] = user_id
        return render(request, 'search/search.html', final_dict)

    else:
        return render(request, 'search/search.html')

    return render(request, 'search/search.html')

def profile(request): # 오른쪽 상단 로그인하면 나오는 프로필에 필요한 데이터를 위한 코드
    username=request.GET['user_id']
    user_info=User.objects.filter(user_id=username).values('user_id','user_email','nickname')[0]
    book_history=BookHistory.objects.filter(user_id=username).values()
    read_book = len(book_history)
    user_info['read_book']=read_book

    return JsonResponse(user_info)


def history_register(request):
    user_id = request.session.get('user_id')
    print('history-user-id',user_id)
    data = {'user_id': user_id}
    if request.method=="GET": # get으로 요청이 오면 html 을 반환
        return render(request,'book_it_up/history.html',data)

    elif request.method =="POST": # post로 요청이오면 해당 내용을 db에 저장하는 코드

        user_id=request.POST.get('read-user-id')
        book_id = request.POST.get('read-book-id')
        score = request.POST.get('star-input')
        start_date = request.POST.get('start')
        end_date = request.POST.get('end')


        res_data ={}


        if not(user_id and book_id and score):

            messages.add_message(request, messages.ERROR, '책 id, 별점을 입력해 주세요')

            return redirect('history_register')
        else: # 중복으로 들어가 오류가 발생하지 않도록 동일한 book_id가 있다면 이미 등록한 책이라 나온다
            history_id='H' + user_id + book_id + 'y'
            db_history_exists=BookHistory.objects.filter(history_id=history_id).exists()
            if db_history_exists:
                messages.add_message(request,messages.ERROR,'이미 등록한 책입니다.')

            else:
                messages.add_message(request, messages.SUCCESS, '등록되었습니다.')
                book_history= BookHistory.objects.create(
                    history_id='H' + user_id + book_id + 'y',
                    user_id=user_id,
                    book_id=book_id,
                    score=score,
                    start_date=start_date,
                    end_date=end_date
                )

                book_history.save()

            return redirect("history_register")

def history(request):
    user_name=request.GET.get('user_id')

    his= BookHistory.objects.filter(user_id=user_name).values() #user_id 컬럼과 같은 값은 모든 값들을 가져와 his 변수에 저장

    try:
        chk=request.GET.get('chk')
        datetime.sleep(1.5)

    except:
        pass

    book_lst= []
    for i in his:
        num=i['book_id']

        total={}
        cover_exists=BookCover.objects.filter(book_id=num).exists() # BookCover에 book_id에 해당되는 커버가 있는지를 변수에 저장
        if cover_exists: # 해당 내용이 있다면 cover_large를 가져오고 book에서 title을 가져온다
            cover_large= BookCover.objects.filter(book_id=num).values('cover_large')
            title=Book.objects.filter(book_id=num).values('title')

            cover_dict={}
            title_dict={}
            for j in cover_large:
                book_dict=j
                cover_dict =dict(i,**j) # 1.책 커버를 담은 딕셔너리를 기존 딕셔너리에 합침
                cover_dict['cover'] = cover_dict.pop('cover_large') # cover_large란

            for k in title:
                title_dict= dict(i,**k) # 2.책 타이틀을 담은 딕셔너리를 기존 딕셔너리에 합침

            result = dict(cover_dict,**title_dict) # 1번과 2번의 결과를 합쳐서 하나의 딕셔너리로 만든다

            book_lst.append(result)

        else: #book_cover에 book_id가 없으면 book테이블에서 cover와 title을 가져온다
            cover= Book.objects.filter(book_id=num).values('cover','title')
            for j in cover:
                book_dict = j

                total = dict(i, **book_dict)  # 두 딕셔너리를 하나로 합치기 위한 코드

            book_lst.append(total)

    json_dict = {'books':book_lst}


    return JsonResponse(json_dict)


def history_update(request):
    user_name=request.GET.get('user_id')
    score=request.GET.get('score')
    start_date=request.GET.get('start_date')
    end_date=request.GET.get('end_date')
    book_id=request.GET.get('book_id')


    book_update = BookHistory.objects.get(user_id=user_name,book_id=book_id) # 북히스토리 모델에서 user_id와 book_id 일치하는 애 가져온다

    #새로 입력한 값으로 업데이트
    book_update.score=score
    book_update.start_date=start_date
    book_update.end_date=end_date

    book_update.save() # 해당 내용을 db에 저장


    data={'result':'성공'}
    return JsonResponse(data) # ajax 응답하려고 넣음


def history_delete(request):
    user_name = request.GET.get('user_id')
    book_id = request.GET.get('book_id')

    book_delete = BookHistory.objects.filter(user_id=user_name,book_id=book_id)
    book_delete.delete()

    data={'result':'성공'}

    return redirect('history_register')


def bestbook(request):

    book_avg = BookHistory.objects.values('book_id').filter(score__gte=4).annotate(score_avg=Avg('score'))

    book_lst=[]

    for i in book_avg:
        title = Book.objects.filter(book_id=i['book_id']).values('title')[0]['title']
        history = BookHistory.objects.filter(book_id=i['book_id'])
        like = LikeTab.objects.filter(book_id=i['book_id'])
        cover_large = BookCover.objects.filter(book_id=i['book_id'])


        if cover_large.exists():
            cover = cover_large.values('cover_large')[0]
            cover['cover'] = cover.pop('cover_large')
        else:
            cover = Book.objects.filter(book_id=i['book_id']).values('cover')[0]
        i['history_cnt'] = len(history)
        i['title'] = title
        i['like_cnt']=len(like)
        i['cover'] = cover.get('cover')

        book_lst.append(i)
    sorted_dict = sorted(book_lst, key=lambda x: (-x['score_avg'], -x['history_cnt'], -x['like_cnt']))

    data ={'books':sorted_dict}
    #print(data)


    return JsonResponse(data)