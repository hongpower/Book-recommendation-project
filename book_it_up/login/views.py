from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import *
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
import json

# 로그인
def index(request):

    if request.method=="GET":
        return render(request,'login/index.html')

    elif request.method=="POST":
        username=request.POST.get("username")
        password = request.POST.get("password")

        res_data = {}
        try:
            user = User.objects.get(user_id=username)
            print('>>>>>>>>>>>>>>>>', check_password(password, user.user_pwd))
            if check_password(password, user.user_pwd):
                # true 일 때
                request.session['user_id'] = username
                return redirect("/")

            else:
                messages.add_message(request, messages.ERROR, '아이디 혹은 비밀번호가 틀립니다')
                return render(request, 'login/index.html')

        except:
            messages.add_message(request, messages.ERROR, '아이디 혹은 비밀번호가 틀립니다')
            return render(request, 'login/index.html')


#회원가입
def signup(request): # 회원가입 코드

    if (request.method =="POST") & (request.POST.get('email') != None):

        username=request.POST.get('username')
        password = request.POST.get('password')
        password_re = request.POST.get('password-re')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        nickname = request.POST.get('nickname')
        birth = request.POST.get('birth')

        res_data ={}

        if not(username and password and password_re and email and gender and nickname and birth):

            messages.add_message(request, messages.ERROR, '모든 정보를 입력해 주세요')

            return redirect('signup')

        elif (len(username) < 7) | (len(username)>14):
            messages.add_message(request,messages.ERROR,'아이디는 8글자 이상, 15글자 이하입니다')
            return redirect('signup')

        elif (username.islower() and any(username.isdigit for username in username))==False:
            messages.add_message(request, messages.ERROR, '아이디는 영어와 숫자의 조합만 가능합니다')
            return redirect('signup')

        elif password != password_re: # 비밀번호 확인
            messages.add_message(request, messages.ERROR, '비밀번호를 확인해 주세요')
            return redirect("signup")

        else: # 모든 조건이 만족할때 회원가입이 완료되고 해당 내용을 db의 user 테이블에 저장

            res_data['success']="회원가입이 완료되었습니다"
            user= User.objects.create(
                user_id=username,
                user_pwd=make_password(password,'key1'),
                user_email=email,
                gender=gender,
                nickname=nickname,
                birth=birth
            )

            user.save()
            return redirect("/login/success")

    # request가 get이라면:
    else:
        return render(request,'login/signup.html')

def success(request):

            return redirect("/login/success")

def success(request): # 회원가입에 성공했을 때

    return render(request,'login/success.html')


def logout(request): # 로그아웃 할때
    request.session.pop('user_id')
    return redirect("/")


def id_chk(request): # id 중복과 제한조건 체크
    user_name=request.GET.get('user_id')

    db_user_exists=User.objects.filter(user_id=user_name).exists()

    json_data={}


    if db_user_exists: # db에 아이디가 존재한다면
        json_data['result']="아이디가 이미 존재합니다"

        return JsonResponse(json_data)
        print('user명', user_name)
        print(len(user_name))

    elif (len(user_name) < 8) | (len(user_name) > 15):
        # messages.add_message(request, messages.ERROR, '아이디는 8글자 이상, 15글자 이하입니다')
        # return redirect('signup')
        json_data['result']='아이디는 8글자 이상, 15글자 이하입니다'
        return JsonResponse(json_data)


    elif (user_name.islower() and any(user_name.isdigit() for user_name in user_name))==False: # 아이디는 영어와 숫자의 조합으로 제한하기 위해 사용
        # messages.add_message(request, messages.ERROR, '아이디는 8글자 이상, 15글자 이하입니다')
        # return redirect('signup')

        json_data['result']='아이디는 영어(소문자)와 숫자의 조합이어야 합니다'
        return JsonResponse(json_data)


    else:
        json_data['result']="사용 가능한 아이디입니다"

        return JsonResponse(json_data)

def nickname_chk(request): # 닉네임 중복,제한 조건 체크
    nickname=request.GET.get('nickname')
    db_nickname_exists=User.objects.filter(nickname=nickname).exists()

    json_data={}


    if db_nickname_exists:
        json_data['result']="별명이 이미 존재합니다"

        return JsonResponse(json_data)

    elif (len(nickname)>7) or (len(nickname)<1):
        json_data['result']='별명은 최대 8자 최소 2자만 가능합니다'
        return JsonResponse(json_data)

    else:
        json_data['result']="사용 가능한 별명입니다"

        return JsonResponse(json_data)


def password_chk(request): # 비밀번호 제한 조건 체크
    password=request.GET.get('password')

    json_data = {}

    if len(password) < 5:
        json_data['result'] = '비밀번호는 6자 이상입니다'
        return JsonResponse(json_data)

    elif password.islower() and any(password.isdigit() for password in password)==False: # 소문자와 숫자 조합이 아니라면
        json_data['result'] = '비밀번호는 소문자(영어)와 숫자의 조합이어야 합니다'
        return JsonResponse(json_data)

    else:
        json_data['result'] = "사용 가능한 비밀번호입니다"

        return JsonResponse(json_data)
















