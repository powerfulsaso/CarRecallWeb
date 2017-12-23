# import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import GasHistory
# Create your views here.


def index(request):
    last_buy = GasHistory.objects.latest('id')
    context = {'last_buy': last_buy,}
    return render(request, 'gasrecall/index.html', context)


def history(request):
    all_buys = GasHistory.objects.all().order_by('-purchase_date')
    context = {'all_buys': all_buys,}
    return render(request, 'gasrecall/history.html', context)


def last_reading(request):
    lr = GasHistory.objects.latest('id')
    response = "<h2>Last Reading</h2><p>{0:s}</p> <p> {1:s} days ago. </p>".format(str(lr), str(lr.days_ago()))
    return HttpResponse(response)
