from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

from mukbang.models import Muckbang
from mukbang.forms import Muckbangform

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


def create(request):
    if request.method == 'POST':
        form = Muckbangform(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/mukbang/list/')
    form = Muckbangform()
    return render(request, 'first/create.html', {'form': form})
def list_test(request):
    context = {

    }
    return render(request, 'mukbang/youtuber_list.html', context)
