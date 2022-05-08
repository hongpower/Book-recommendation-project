from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import *
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages



# 로그인
def index(request):

    if request.method=="GET":
        return render(request,'login/index.html')
    elif request.method=="POST":
        username=request.POST.get("username")
        password = request.POST.get("password")

        print(username)

        res_data = {}
        try:

            user = User.objects.get(user_id=username, user_pwd=make_password(password,'key1'))
        except:

            messages.add_message(request, messages.ERROR, '아이디 혹은 비밀번호가 틀립니다')

            return render(request, 'login/index.html')
        request.session['user_id']=username


        return redirect("/")



#회원가입
def register(request):
    if request.method=="GET":
        return render(request,'login/register_parct.html')
    elif request.method =="POST":
        #회원가입 코드
        # username= request.POST['username']
        # print(username)
        # password= request.POST['password']
        # password_re=request.post['password-re']
        # email=request.POST['eamil']
        # gender = request.POST['gender']
        # nickname = request.POST['nickname']
        # birth = request.POST['birth']
        username=request.POST.get('username')
        password = request.POST.get('password')
        password_re = request.POST.get('password-re')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        nickname = request.POST.get('nickname')
        birth = request.POST.get('birth')
        print(username)
        print(password)

        res_data ={}

        if not(username and password and password_re and email and gender and nickname and birth):

            messages.add_message(request, messages.ERROR, '모든 정보를 입력해 주세요')

            return redirect('register')


        elif password != password_re:
            messages.add_message(request, messages.ERROR, '비밀번호를 확인해 주세요')
            return redirect("register")

        else:

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
            print(res_data)
            return redirect("/login/success")



def success(request):
    return render(request,'login/success.html')


def logout(request):
    request.session.pop('user_id')
    return redirect("/")

# 이미지를 랜덤하게 20개를 가져와
# 옆에 따봉(좋아요) ,따봉(싫어요) 뒤집힌거 ,하트(찜) 모양
# 따봉인애를 누르면 db like 유저의 like id ,uset_id, book_id
#
# kim 책1 좋아요
#
# 좋아요     아이디     책 아이디
# 1         kim         책1
# 2         kim         책2
# 3         jo          책1


















