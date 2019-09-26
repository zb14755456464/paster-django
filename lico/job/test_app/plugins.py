# Copyright 2019-present Lenovo
# Confidential and Proprietary

import logging


from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header,
)
from rest_framework import exceptions

logger = logging.getLogger(__name__)

class MyAuthentication(BaseAuthentication):
    def authenticate(self,request):
        token = request._request.GET.get('token')
        # 获取用户名和密码，去数据校验
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')
        print (1111111111111111111111111)
        print (1111111111111111111111111)
        print (1111111111111111111111111)
        print (1111111111111111111111111)
        return ("dog", None)

    def authenticate_header(self,val):
        pass