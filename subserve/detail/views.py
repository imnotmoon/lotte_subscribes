import json
import os
from django.shortcuts import render, redirect
from store.models import Store
from menu.models import Menu
from django.http import HttpResponse
from customer.models import Customer
from sublist.models import Subscribes
from django.contrib.auth.models import User
from .forms import StoreForm
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import datetime
# Create your views here.
def detail(request, storeID) :
    #store = Store.objects.filter(id = storeID)
    store = Store.objects.get(id= storeID)
    #저장된 매장중에 검색한 매장 찾기
    jsonPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'subserve/keys.json')
    with open(jsonPath, 'r') as f:
        keys = json.load(f)
    mapKey = keys['kakaomap-api']
    context = {'store' : store, 'key' : mapKey}
    return render(request, 'detail.html', context)
    #return render(request, 'detail.html', {'storeID' : storeID, 'key' : mapKey})

def create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save(commit=False)
            store.save()
            return redirect('/')
    else:
        form = StoreForm()
    return render(request, 'store_form.html', {'form': form})

def purchasing(request, menu_id, store_id) :
    menuContext = Menu.objects.get(menu_id=menu_id, store_id=store_id)
    return render(request, 'purchasing.html', {'menu': menuContext})

def subscribe(request,menu_id, store_id):
    menuContext = Menu.objects.get(menu_id=menu_id, store_id=store_id)
    user = request.POST.get('user')
    return render(request, 'subscribe.html', {'menu': menuContext,'user':user})

def submenu(request,menu_id, store_id):
    menuContext = Menu.objects.get(menu_id=menu_id, store_id=store_id)
    #user = Customer.objects.get(id=user_id)
    user= request.user
    current = datetime.now()
    s = Subscribes(user_id=user.customer, store_id=menuContext.store_id, menu_id=menuContext,
    start_date = current, end_date = current+relativedelta(months=1), remain = menuContext.count)
    s.save()
    return render(request,'submenu.html',{'menu':menuContext, 'user':user})

def checkAvailable(request) :
    # get data from body
    userID = request.POST.get('userid')
    storeID = request.POST.get('store')
    menuID = request.POST.get('menu')
    count = request.POST.get('count')

    isUserExist = False
    isSubListExist = False
    isRemainExist = False
    remain = 0

    # scneario 1. check if user is exist
    try:
        user = Customer.objects.get(id = userID)
        isUserExist = True
    except Customer.DoesNotExist :
        return HttpResponse(json.dumps({
            'result' : 'UserDoesNotExist'
        }), status = 500)

    # scenario 2. check if sublist is exist
    try:
        sublist = Subscribes.objects.get(menu_id=menuID, storeID=storeID, userID=userPhone)
        isSubListExist = True
        # scenario 3. substract remaining counts
        if sublist.remain > 0 :
            sublist.remain -= 1
            sublist.save()
        else :
            return HttpResponse(json.dumps({
            'result' : 'UserHaveNoRemainCounts'
        }), status = 501)
    except :
        return HttpResponse(json.dumps({
            'result' : 'UserDidNotSubscribed'
        }), status = 502)
