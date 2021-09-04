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

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'youtuber': items
    }

    return render(request, 'first/list.html ', context)