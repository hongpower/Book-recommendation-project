from django.shortcuts import render
from .models import *
from pymongo import MongoClient
import random
from django.http import HttpResponse, JsonResponse

client = MongoClient("mongodb://seongheon:%40cshun1006@59.6.7.229:27018")

def rcm(request):
    # 1) user_id 겟 하기
    user_id = request.session.get('user_id')

    # 2) 사용자가 좋아요한 책들 다 가져오기
    like_books = LikeTab.objects.filter(user_id=user_id).values()
    like_isbn = list()

    for book in like_books:
        like_isbn.append(book['book_id'])

    # 3) 해당 책들의 유사한 책들 담아오기
    db = client.book
    collection = db.relative_book

    rel_books = collection.find({'isbn13': {"$in":like_isbn}})

    # rel_books는 무슨 모습일까?
    rel_books_lst = list()

    # 4) 유사한 책들의 isbn 담기
    for book in rel_books:
        for i in range(10):
            try:
                rel_book_isbn = (book['books'])[i]
                rel_books_lst.append(rel_book_isbn)
            except:
                break

    # 5) 사용자가 싫어했던 책이 포함되면 제외하기
    dislike_books = DislikeTab.objects.filter(user_id=user_id).values()

    for book in dislike_books:
        if book['book_id'] in like_isbn:
            dislike_idx = like_isbn.index(book['book_id'])
            like_isbn.pop(dislike_idx)
    # 7) 유사한 책들의
    # 6) 유사한 책들의 이미지 가져오기
    rel_books_cover_lst = list()
    final_dict = dict()

    final_books = BookCover.objects.filter(book_id__in=rel_books_lst)
    for book in final_books:
        temp = dict()
        temp['book_id'] = book.book_id
        temp['img_url'] = book.cover_large
        rel_books_cover_lst.append(temp)
    final_dict['rcm_books'] = rel_books_cover_lst

    final_dict['user_id'] = user_id

    return render(request, 'rcm/rcm.html', final_dict)


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


## 성헌:

def mysite(request):
    return render(request, 'book_it_up/mysite.html')


def test(request):
    return render(request, 'book_it_up/mysite.html')


def book_photo(request):
    books = request.GET['book_photo']
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