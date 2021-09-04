from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

from mukbang.models import Muckbang,Group
from mukbang.forms import Muckbangform, Groupform

import random

from django.http import HttpResponseRedirect
from django.db.models import Count, Avg
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    now = datetime.now()
    context = {
        'current_date':now
    }
    return render(request, 'first/index.html', context)

def list(request):
    youtuber = Muckbang.objects.all()
    paginator = Muckbang(youtuber, 5)

    items = paginator

    context = {
        'youtuber': items
    }

    return render(request, 'first/list.html ', context)

def test(request):
    context = {

    }
    return render(request, 'mukbang/main.html',context)


def create(request, group_id):
    if request.method == 'POST':
        form = Muckbangform(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/mukbang/group_list/')

    item = get_object_or_404(Group, pk=group_id)
    form = Muckbangform(initial={'group': item})

    return render(request, 'first/create.html', {'form': form, 'item': item})


def list_test(request):
    context = {
    }
    return render(request, 'mukbang/youtuber_list.html', context)


def group_list(request):
    groups = Group.objects.all()

    context = {
    }
    return render(request, 'mukbang/group_list.html', {'context' : context, 'groups': groups})

def youtuber(request, group_id):
    youtubers = Muckbang.objects.all().filter(group = group_id)
    paginator = Paginator(youtubers, 10)

    page = request.GET.get('page') ## third/list?page=1
    items = paginator.get_page(page)

    group = Group.objects.all()[group_id-1]

    context = {
        'youtubers': items,
        
    }
    return render(request, 'mukbang/youtuber.html', {'context' : context, 'group': group})

def question1(request):
    context ={

    }
    return render(request, 'mukbang/question.html', context)


def update(request):
    if request.method == 'POST' and 'id' in request.POST:
        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Muckbang, pk=request.POST.get('id'))
        # password = request.POST.get('password', '')
        form = Muckbangform(request.POST, instance=item)
        if form.is_valid() :
            item = form.save()
    elif request.method == 'GET':
        # item = Restaurant.objects.get(pk=request.GET.get('id'))  ##third/update?id=2
        item = get_object_or_404(Muckbang, pk=request.GET.get('id'))
        form = Muckbangform(instance=item)
        return render(request, 'first/update.html', {'form': form})
    return HttpResponseRedirect('/mukbang/group_list/')

def result(request):
    context ={

    }
    return render(request, 'mukbang/result.html', context)

def question2(request):
    context ={
    }
    return render(request, 'mukbang/notready.html', context)

