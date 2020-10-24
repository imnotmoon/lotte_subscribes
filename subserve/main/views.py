from django.shortcuts import render
import os
import json
from store.models import Store
from menu.models import Menu
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User
from sublist.models import Subscribes


# Create your views here.
def main(request):
    stores=Store.objects.all()
    return render(request, 'main.html', {'stores' : stores} )


def search(request):
    stores=Store.objects.all().order_by('-id')
    menus = Menu.objects.all().order_by('-menu_id')
    q = request.POST.get('q',"")

    if q:
        stores=stores.filter(storename__icontains=q)
        menus= menus.filter(menu_name__icontains=q)
        return render(request, 'search.html', {'stores' : stores, 'menus' : menus, 'q' : q})
    else:
        return render(request, 'search.html')

def mylocation(request) :
    jsonPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'subserve/keys.json')
    with open(jsonPath, 'r') as f:
        keys = json.load(f)
    mapKey = keys['kakaomap-api']
    return render(request, 'mylocation.html', {'key' : mapKey})

def login(request) :
    return render(request, 'login.html')
    
def loadMoreData(request) :
    # scenario 1. get data from request body
    count = request.POST.get('count', 0)
    stores = Store.objects.all()
    ret = serializers.serialize('json', stores)
    print(ret)
    return HttpResponse(ret, content_type="text/json-comment-filtered")

def sidebarData(request) :
    # 1. sublist
    ret = []
    print(request.user)
    try :
        userid = request.user.customer.id
        sublist = Subscribes.objects.filter(user_id=userid)
        print(sublist)
        for sub in sublist :
            print(sub.end_date)
            temp = dict()
            temp['store_id'] = sub.store_id
            temp['menu_id'] = sub.menu_id
            temp['name'] = sub.__str__()
            temp['split'] = temp['name'].split(' -- ')
            temp['endDate'] = sub.end_date
            ret.append([temp['split'][1], str(temp['endDate'])])
        print(ret)
    except :
        ret = []
    
    # 2. wishlist

    return HttpResponse(json.dumps(ret), content_type="text/json-comment-filtered")

def weekrank(request) :
    stores = Store.objects.all().order_by('rank')[:10]
    return render(request, 'weekrank.html', {'stores' : stores})

def manager(request) :
    return render(request, 'manager.html')