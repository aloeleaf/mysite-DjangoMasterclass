from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.template import loader


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
       'item_list':item_list
    }
    return render (request,'food/index.html',context)

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item
    }
    return render(request,'food/detail.html',context)


    return HttpResponse("This is item no/id: %s" %item_id)
