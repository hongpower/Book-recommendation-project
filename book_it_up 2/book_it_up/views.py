from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import random
from pymongo import MongoClient

client = MongoClient("mongodb://jisu:%40ghdwltn1@59.6.7.229:27018")


def index(request):
    # 짧은 책 랜덤으로 불러오기, page수 150이하, 무게 150이하, 높이 150이하, 가로길이 150이하로 0/null 아닌 값  :
    books = BookSize.objects.filter(width__lte=200, height__lte=200, page__lte=200, weight__lte=200)
    book_lst = []
    for i in range(15):
        rand_n=random.randint(0, len(books))
        book_lst.append(books[rand_n].book_id)
    final_lst = list()
    final_dict = dict()
    books = BookCover.objects.filter(book_id__in=book_lst)
    for book in books:
        temp = dict()
        temp['book_id'] = book.book_id
        temp['img_url'] = book.cover_large
        final_lst.append(temp)
    final_dict['short_books'] = final_lst

    user_id = request.session.get('user_id')
    if user_id:
        print(user_id)
        print("로그인정보성공")
        final_dict['user_id']=user_id
    else:
        print("없음")
    # 리뷰 많은 순서의 책 불러오기 :
    print(final_dict, "이건 원본")
    return render(request, 'book_it_up/index.html', final_dict)


def book_id(request):
    book_id = request.GET['bookId']

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
    print(score)
    top_box_info['score'] = score
    
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
    desc = BookDesc.objects.filter(book_id=book_id).values("description1")[0]['description1']
    print(desc)
    bottom_box_info['desc'] = desc
    
    # 리뷰(mongo)
    collection = db.review
    reviews = collection.find({'book_id': book_id})

    review_lst = list()
    for review in reviews:
        review_lst.append(review['review'])
    bottom_box_info['review'] = review_lst
    print(review_lst)

    # phrase
    phrase_lst = list()
    phrases = Phrase.objects.filter(book_id=book_id).values("phrase_content")
    for phrase in phrases:
        phrase['phrase_content'].replace("  ", "")
        phrase_lst.append(phrase['phrase_content'])
    bottom_box_info['phrase'] = [phrase_lst]
    print(phrase_lst)

    total_box_info = dict()
    total_box_info['all'] = [top_box_info, bottom_box_info]
    print(total_box_info)
    return JsonResponse(total_box_info)

def mysite(request):
    return render(request,'book_it_up/mysite.html')


def test(request):
    return render(request,'book_it_up/mysite.html')


def book_photo(request):
    books = request.GET['book_photo']
    list1 = []
    for i in range(1, 11):
        num = random.randint(0, 233862)
        list1.append(num)
    print(list1)

    dic_data = []
    book_info = Book.objects.values('book_id', 'cover')
    print(type(book_info))
    for j in list1:
        data = book_info[j]
        dic_data.append(data)
    print(dic_data)
    json_data = {'books': dic_data}

    return JsonResponse(json_data)


