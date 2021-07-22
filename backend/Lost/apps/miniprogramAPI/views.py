import requests
import json

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class Auth(object):
    appId = "[数据删除]"
    appSecret = "[数据删除]"

    def getAccessToken(self):
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + self.appId + "&secret=" + self.appSecret
        return_value = requests.get(url)
        print(return_value.json())
        try:
            access_token = return_value.json()['access_token']
            expires_in = return_value.json()['expires_in']
        except Exception:
            errcode = return_value.json()['errcode']
            errmsg = return_value.json()['errmsg']
        else:
            return access_token


class Security(object):

    def imgSecCheck(self, img):
        access_token = Auth().getAccessToken()
        url = "https://api.weixin.qq.com/wxa/img_sec_check?access_token=" + access_token
        file = {'file': img}
        return_value = requests.post(url=url, files=file)
        return_value_json = return_value.json()
        print(return_value_json)
        errcode = return_value_json['errcode']
        errmsg = return_value_json['errmsg']
        if errcode == 87014:
            return False
        else:
            return True

    def multiImgSecCheck(self, imglist):
        for img in imglist:
            if not Security().msgSecCheck(img=img):
                return False
        return True

    def msgSecCheck(self, msg):
        access_token = Auth().getAccessToken()
        url = "https://api.weixin.qq.com/wxa/msg_sec_check?access_token=" + access_token
        data = {'content': msg}
        return_value = requests.post(url=url, data=json.dumps(data))
        return_value_json = return_value.json()
        print(return_value_json)
        errcode = return_value_json['errcode']
        errmsg = return_value_json['errmsg']
        if errcode == 87014:
            return False
        else:
            return True

    def multiMsgSecCheck(self, msglist):
        for msg in msglist:
            if not Security().msgSecCheck(msg=msg):
                return False
        return True


class Test(APIView):
    def get(self, request):
        image = open("[数据删除]", "rb")
        value = Security().imgSecCheck(img=image)
        return Response({'value': value})
