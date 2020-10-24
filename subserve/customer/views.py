from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Customer
from .models import Manager
from sublist.models import Subscribes
from menu.models import Menu
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.
def signUp(request) :
    return render(request, 'signup.html')

def signIn(request) :
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        isManager = request.POST["isManager"]
        # 매니저면 1, 아니면 null
        print(isManager)
        if len(isManager) != 0 :
            print("ASDF?ASDF?ADSF?AS?DFA?SD?")
            customer = auth.authenticate(request, username = username, password = password)
            if customer is not None:
                auth.login(request,customer)
                print(customer.username)
                return redirect("/")
            else:
                return render(request, 'signin.html', {'error': "There is No user"})
                # Manager 객체랑 대조해서 로그인.
        else :
            print("MANAGERMAANAGER")
            manager = auth.authenticate(request, username=username, password=password)
            if manager is not None :
                auth.login(request, manager)
                print(manager.username)
                return redirect("/manager")    # 이거말고 매니저용 웹
    else:
        return render(request, 'signin.html')



def myPage(request) :
    return render(request, 'mypage.html')

def editProfile(request) :
    return render(request, 'editprofile.html')

def findAccount(request) :
    return render(request, 'findaccount.html')

def confirmPassword(request) :
    return render(request, 'confirmpassword.html')

def resign(request) :
    return render(request, 'resign.html')

def signUpAPI(request) :
    print(request.POST['pwd'])
    # scenario 1. check every values correct
    if request.POST.get('pwd')!=request.POST.get('pwdconfirm'):
        print("wrong password")
        return JsonResponse({
            'status' : 'false',
            'message' : "비밀번호가 서로 다릅니다.",
        }, status=500)

    try:
        user = Customer.objects.get(name = request.POST.get('id', ''))
        print("id already been taken")
        return JsonResponse({
            'status' : 'false',
            'message' : "Id already been taken"
        }, status=500)

    except Customer.DoesNotExist:
        user = User.objects.create(username = request.POST.get('id', ''), email = request.POST.get('email', ''))
        user.set_password(request.POST.get('pw', ''))
        user.save()

        # 유저 생성 및 연결
        name = request.POST.get('name', '')
        if request.POST.get('sex', '')=="male":
            sex = 1
        else:
            sex = 0
        address = request.POST.get('address', '')
        birthday = request.POST.get('birthday', '')
        phone = request.POST.get('phone', '')

        # 마케팅 정보 수신 동의 내용
        if request.POST.get('marketing-email', '') == 'true':
            marketingEmail = 1
        else :
            marketingEmail = 0
        if request.POST.get('marketing-sms', '') == 'true' :
            marketingSMS = 1
        else :
            marketingSMS = 0
        marketingSMS = request.POST.get('marketing-sms')
        customer = Customer(name= name, address = address, birthday = birthday, phone = phone, sex = sex, marketing_email = marketingEmail, marketing_sms = marketingSMS)
        customer.user = user
        customer.save()
        auth.login(request, user)
        return HttpResponse(status=200)


def loginAPI(request) :
    print(request.POST)
    print("loginAPI")
    userID = request.POST.get('id')
    userPW = request.POST.get('pw')
    isManager = request.POST.get('isManager')
    print(isManager)
    # 매니저면 1, 아니면 null
    user = auth.authenticate(request, username=userID, password = userPW)
    if user is not None:
        auth.login(request, user)
        if isManager != '1' :
            return redirect('/')
        else :
            print("MANAGER")
            menu = Menu.objects.filter(store_id=user.manager.store)

            subCount = []
            for m in menu :
                sublists = Subscribes.objects.filter(menu_id=m.menu_id).count()
                subCount.append(sublists)

            return render(request, 'manager.html', {'store':user.manager.store, 'menu': menu, 'countSub': subCount})
    else:
        return render(request, 'mypage.html', {'error' : 'id나 비밀번호를 다시 확인해주세요'})
    

def logout(request) :
    print("ASDFASDFA")
    auth.logout(request)
    return redirect('/')


def editProfileAPI(request) :
    address = request.POST.get('address')
    phone = request.POST.get('phone')

    # 유저정보 가져와서 업데이트하는 쿼리

    return render(request, 'mypage.html')