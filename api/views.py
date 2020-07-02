from django.contrib.auth.models import Group, Permission
from django.shortcuts import render

# Create your views here.

from rest_framework.generics import GenericAPIView

from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet

from api.authentications import MyAuth
from api.models import User
from api.throttle import SendMessageRate
from untls.response import APIResponse


class TestAPIView(APIView):
    def get(self,request,*args,**kwargs):
        # return APIResponse("成功查询")
        #获取用户
        # user = User.objects.first()
        # print(user)
        # #根据用户获取角色（groups）
        # group = user.groups.first()
        # print(group)
        # #根据用户获取用户相对应的权限 (permissions)
        # permissions = user.user_permissions.first().name
        # print(permissions)

        #获取角色（group）
        # groups = Group.objects.first()
        # print(groups)
        # #根据角色获取用户对应的权限 （permissions）
        # permissions = groups.permissions.first().name
        # print(permissions)
        # #根据角色获取用户（user）
        # user = groups.user_set.first().username
        # print(user)


        #获取权限
        permission = Permission.objects.filter(pk=8).first()
        print(permission.name)
        #根据权限获取用户 （user--->admin） 获取的必须是权限，而不是权限的名字
        user = permission.user_set.first().username
        print(user)
        #根据权限获取角色（group--->管理者）
        #必须先获取与角色相关联的权限（而不是用户user的权限），才能根据权限获取相对应的角色
        permission_group = Permission.objects.filter(pk=9).first()
        group = permission_group.group_set.first().name
        print(group)
        return APIResponse("成功查询")

class TestPermissionAPIView(APIView):
    """
    只有认证后的才可以访问
    """
    authentication_classes = [MyAuth]  #局部配置
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return APIResponse("登录访问成功")


class UserLoginOrReadOnly(APIView):
    #登录是写操作，需要进行验证，查看则都能查看
    throttle_classes = [UserRateThrottle]

    # permission_classes = [MyPermission]

    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作访问成功")


class SendMessageAPIView(APIView):
    throttle_classes = [SendMessageRate]

    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作访问成功")
