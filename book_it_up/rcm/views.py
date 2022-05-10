from django.shortcuts import render
from .models import *
from pymongo import MongoClient
import random
from django.http import HttpResponse, JsonResponse
from .secrets import mongo_user, mongo_pw, ip_address, port_num

client = MongoClient("mongodb://" + mongo_user + ":" + mongo_pw + "@" + ip_address + ":" + port_num)


def rcm(request):
    # 1) user_id 겟 하기
    user_id = request.session.get('user_id')

    # 2) 사용자가 좋아요한 책들 + 위시리스트 책들 다 가져오기,
    category_ratio_dict = dict()

    like_books = LikeTab.objects.filter(user_id=user_id).values()
    like_isbn = list()
    for book in like_books:
        like_isbn.append(book['book_id'])

    wishlist_books = Wishlist.objects.filter(user_id=user_id).values()
    for book in wishlist_books:
        like_isbn.append(book['book_id'])

    # 3) 사용자가 좋아요했던/위시리스트에 담은 책들을 기준으로
    #   1. 평점 높은 기준 & 최근거 위주로 order by
    temp = list(BookGrade.objects.filter(book_id__in=like_isbn).order_by('-score').values("book_id"))
    like_isbn = list(isbn['book_id'] for isbn in temp)

    #   2. 좋아요 장르 비율 계산하기
    temp = list(Book.objects.filter(book_id__in=like_isbn))

    total_books_n = 0
    for book in temp:
        category_name = book.category.split('>')[0]
        if category_name not in category_ratio_dict.keys():
            category_ratio_dict[category_name]= []
            category_ratio_dict[category_name].append(1)
            total_books_n += 1
            category_ratio_dict[category_name].append([])
            category_ratio_dict[category_name][1].append(book.book_id)
        else:
            category_ratio_dict[category_name][0] += 1
            total_books_n += 1
            category_ratio_dict[category_name][1].append(book.book_id)

    for category in category_ratio_dict.keys():
        category_num = category_ratio_dict[category][0]
        category_ratio_dict[category].append(round((category_num/total_books_n)*20))

    like_isbn = list()

    # 4) 비율만큼만 찾아오기
    for category in category_ratio_dict.keys():
        category_ratio = category_ratio_dict[category][2]
        for i in range(category_ratio):
            like_isbn.append(category_ratio_dict[category][1][i])

    ## 유사하지 않은 책 가져오는 함수:
    unrel_books_cover_lst = get_opposite_type_books(like_isbn, user_id)

    # 5) 해당 책들의 유사한 책들 담아오기
    db = client.book
    collection = db.unrelative_book

    rel_books = collection.find({'isbn13': {"$in":like_isbn}})

    rel_books_lst = list()

    # 6) 유사한 책들의 isbn 담기 (10개 정도)
    for book in rel_books:
        for i in range(10):
            try:
                rel_book_isbn = (book['books'])[i]
                rel_books_lst.append(rel_book_isbn)
            except:
                break

    # 7) 사용자가 싫어했던 책이 포함되면 제외하기
    dislike_books = DislikeTab.objects.filter(user_id=user_id).values()

    for book in dislike_books:
        if book['book_id'] in like_isbn:
            dislike_idx = like_isbn.index(book['book_id'])
            rel_books_lst.pop(dislike_idx)

    # 8) 유사한 책들의 이미지 가져오기 & 랜덤으로 100개만 중복없이 뽑기
    rel_books_cover_lst = list()
    final_dict = dict()

    final_books = BookCover.objects.filter(book_id__in=rel_books_lst)

    rand_n = random.sample(range(len(final_books)), 100)

    # 5개씩 한 세트로 묶어서 넣기 위함 :
    for i in range(0,100, 5):
        five_books_lst = list()
        for j in rand_n[i:i+5]:
            book = final_books[j]
            temp = dict()
            temp['book_id'] = book.book_id
            temp['img_url'] = book.cover_large
            five_books_lst.append(temp)

        rel_books_cover_lst.append(five_books_lst)

    final_dict['different_books'] = unrel_books_cover_lst
    final_dict['rcm_books'] = rel_books_cover_lst

    final_dict['user_id'] = user_id

    print(final_dict['rcm_books'])
    return render(request, 'rcm/rcm.html', final_dict)


def get_opposite_type_books(like_isbn, user_id):
    db = client.book
    collection = db.unrelative_book

    unrel_books = collection.find({'isbn13': {"$in": like_isbn}})

    unrel_books_lst = list()

    # 유사하지 않은 책 담기:
    for book in unrel_books:
        for i in range(10):
            try:
                unrel_book_isbn = (book['books'])[i]
                unrel_books_lst.append(unrel_book_isbn)
            except:
                break

    # 7) 사용자가 싫어했던 책이 포함되면 제외하기
    dislike_books = DislikeTab.objects.filter(user_id=user_id).values()

    for book in dislike_books:
        if book['book_id'] in like_isbn:
            dislike_idx = like_isbn.index(book['book_id'])
            unrel_books_lst.pop(dislike_idx)

    # 8) 비유사한 책들의 이미지 가져오기 & 랜덤으로 100개만 중복없이 뽑기
    unrel_books_cover_lst = list()
    final_dict = dict()

    final_books = BookCover.objects.filter(book_id__in=unrel_books_lst)

    rand_n = random.sample(range(len(final_books)), 100)

    # 5개씩 한 세트로 묶어서 넣기 위함 :
    for i in range(0, 100, 5):
        five_books_lst = list()
        for j in rand_n[i:i + 5]:
            book = final_books[j]
            temp = dict()
            temp['book_id'] = book.book_id
            temp['img_url'] = book.cover_large
            five_books_lst.append(temp)

        unrel_books_cover_lst.append(five_books_lst)

    return unrel_books_cover_lst


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

def get_topic(request):
    user_id = request.session.get('user_id')

    # 1) 키워드 리스트 랜덤으로 10개 정도 뽑아오기
    db = client.book
    collections = db.topic

    topic_lst = list(list(topic.keys())[1] for topic in collections.find())

    rand_n = random.sample(range(len(topic_lst)), 10)
    final_topic_lst = list()

    for n in rand_n:
        final_topic_lst.append(topic_lst[n])

    final_dict = dict()
    final_dict['user_id'] = user_id
    final_dict['topic_lst'] = final_topic_lst

    return render(request, 'rcm/keyword.html', final_dict)

# 사용자가 토픽 고르고 버튼 누르면 추천해주는 함수
def get_topic_rcm(request):
    user_id = request.GET.get('user_id')

    # ary 타입 받기 위해서는 [] 활용
    topic_lst = request.GET.getlist('topic_lst[]')

    # 추천 isbn이 담길 리스트:
    isbn_lst = list()

    # db에서 받아오기
    db = client.book
    collections = db.topic

    for topic in topic_lst:
        ele = collections.find()
        for e in ele:
            try:
                isbn_lst += e[topic]
                break
            except:
                pass

    rand_n = random.sample(range(len(isbn_lst)), 60)
    final_isbn_lst = list()
    topic_books_cover_lst = list()

    for n in rand_n:
        final_isbn_lst.append(isbn_lst[n])

    final_books = BookCover.objects.filter(book_id__in=final_isbn_lst)

    # 5개씩 한 세트로 묶어서 넣기 위함 :
    for i in range(0, 50, 5):
        five_books_lst = list()
        for j in range(i, i+5):
            book = final_books[j]
            temp = dict()
            temp['book_id'] = book.book_id
            temp['img_url'] = book.cover_large
            five_books_lst.append(temp)

        topic_books_cover_lst.append(five_books_lst)

    final_dict = dict()

    final_dict['topic_books'] = topic_books_cover_lst
    final_dict['user_id'] = user_id

    return JsonResponse(final_dict)


