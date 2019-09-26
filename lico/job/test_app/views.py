#coding:utf-8
from django.http import HttpResponse
from rest_framework.views import APIView
import json


class DogView(APIView):

    def get(self,request,*args,**kwargs):
        print(request)
        print(request.user)
        ret  = {
            'code':1000,
            'msg':'xxx'
        }
        return HttpResponse(json.dumps(ret),status=201)