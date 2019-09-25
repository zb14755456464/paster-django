#coding:utf-8
from django.http import HttpResponse
from django.conf import settings


def index(request):
    print(settings.DEBUG)
    return HttpResponse("index")