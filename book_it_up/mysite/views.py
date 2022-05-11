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

# 내정보 확인하는 페이지 연결해주는 함수 :
def mysite(request):
    user_id = request.session.get('user_id')
    data={'user_id':user_id}
    return render(request,'mysite/mysite.html',data)

def mysite_likebook(request):  #mysite에서 likebook 표지들 가져오기
    user_id = request.GET.get('user_id')

    likebook = LikeTab.objects.filter(user_id=user_id).values() # user_id와 같은 user에 해당하는 데이터들을 가져와 변수에 저장

    like_lst = []
    for i in likebook:
        num = i['book_id']
        cover = BookCover.objects.filter(book_id=num).values('cover_large','book_id')[0]
        like_lst.append(cover)

    json_dict = {'books': like_lst}

    return JsonResponse(json_dict)


def mysite_wishlistbook(request): # mysite에서 wishlist 표지들 가져오기
    user_id = request.GET.get('user_id')

    wishlistbook = Wishlist.objects.filter(user_id=user_id).values() # user_id와 같은 user에 해당하는 데이터들을 가져와 변수에 저장

    wishlist_lst = []
    for i in wishlistbook:
        num = i['book_id']
        cover = BookCover.objects.filter(book_id=num).values('cover_large','book_id')[0]
        wishlist_lst.append(cover)

    json_dict = {'books': wishlist_lst}

    return JsonResponse(json_dict)


def all_like(request):
    user_id = request.session.get('user_id')

    data={'user_id':user_id}
    return render(request,'book_it_up/all_like.html',data)

def all_wish(request):
    user_id = request.session.get('user_id')
    data={'user_id':user_id}
    return render(request,'book_it_up/all_wishlist.html',data)

def user_info(request):
    user_id = request.GET.get('user_id')

    mysite_user = User.objects.filter(user_id=user_id).values()[0]
    return JsonResponse(mysite_user)

def mysite_update(request):
    user_id = request.GET.get('user_id')
    user_email = request.GET.get('email')
    gender = request.GET.get('gender')
    birth = request.GET.get('birth')


    user_update = User.objects.get(user_id=user_id)  # 유저 모델에서 user_id 일치하는 애 가져온다

    # 새로 입력한 값으로 업데이트
    user_update.user_email = user_email
    user_update.gender= gender
    user_update.birth = birth

    user_update.save()  # 해당 내용을 db에 저장

    data = {'result': '성공'}
    return JsonResponse(data)  # ajax 응답하려고 넣음


def usage(request):
    user_id = request.GET.get('user_id')
    like= LikeTab.objects.filter(user_id=user_id)
    dislike=DislikeTab.objects.filter(user_id=user_id)
    wish=Wishlist.objects.filter(user_id=user_id)
    history=BookHistory.objects.filter(user_id=user_id)

    data = {'like':len(like),'dislike':len(dislike),'total':len(like)+len(dislike),'wishlist':len(wish),'history':len(history)}
    for d in data:
        if data[d]=="undefined":
            data[d] == 0

    return JsonResponse(data)


def mysite_board(request):
    user_id = request.GET.get('user_id')
    board = Board.objects.filter(user_id=user_id).values()

    board_lst =[]
    for i in board:
        board_lst.append(i)

    data = {'board':board_lst}
    print(data)
    return JsonResponse(data)