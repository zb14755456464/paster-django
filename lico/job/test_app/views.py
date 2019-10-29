# coding:utf-8
import json

from django.http import HttpResponse
from rest_framework.views import APIView

from lico.job.test_app.models import Human


class DogView(APIView):

    def get(self, request, *args, **kwargs):
        ret = {
            'code': 1000,
            'msg': 'xxx'
        }
        return HttpResponse(json.dumps(ret), status=201)


class HuamanCreate(APIView):

    def post(self, request):
        Human.objects.create(
            name='zhangbiao',
            age=12
        )
        return HttpResponse(status=201)
