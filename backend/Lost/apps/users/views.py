import requests

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer

# Create your views here.
# 使用APIView


class Register(APIView):
    def post(self, request):
        try:
            student = Student.objects.get(studentID=request.data.get('studentID'))
            if student.name.strip() == request.data.get('name').strip():
                student.openID = request.data.get('openid')
                student.save()
                return Response({'name': student.name.strip(), 'studentID': student.studentID},
                                status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        code = request.data.get('code')
        openid = GetOpenid().get_openid(code)

        try:
            student = Student.objects.get(openID=openid)
        except Exception:
            student = None

        if student:
            return JsonResponse({'message': 'success', 'name': student.name.strip(), 'studentID': student.studentID})
        else:
            return JsonResponse({'message': 'fail', 'openid': openid})


class GetOpenid(object):
    url = "https://api.weixin.qq.com/sns/jscode2session?"
    appId = "[数据删除]"
    appSecret = "[数据删除]"

    def get_openid(self, code):
        url = self.url+"appid="+self.appId+"&secret="+self.appSecret+"&js_code="+code+"&grant_type=authorization_code"
        return_value = requests.get(url)
        try:
            openid = return_value.json()['openid']
            session_key = return_value.json()['session_key']
            # print(openid, session_key)
        except Exception:
            # errcode = return_value.json()['errcode']
            print(return_value.json())
            return None
        else:
            return openid


'''
class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
'''
