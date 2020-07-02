from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from api.models import User

class MyAuth(BaseAuthentication):
    """
    在前端发送请求携带认证信息  必须按照一定的格式来
    默认使用Authorization携带认证信息
    认证信息都包含在 request.META字段中
    """

    # 重写authenticate
    def authenticate(self, request):
        # 获取认证信息
        auth = request.META.get('HTTP_AUTHORIZATION', None)
        print(auth)

        if auth is None:
            # 代表游客
            return None

        # 设置认证信息的校验规则   "auth 认证信息"
        auth_list = auth.split()

        # 校验规则：是否是合法用户  是不是两段式  如果第一个不是auth就错误
        if not (len(auth_list) == 2 and auth_list[0].lower() == "auth"):
            raise exceptions.AuthenticationFailed("认证信息有误，认证失败")

        # 如果认证成功 则解析用户  规定认证信息必须为abc.admin.123
        if auth_list[1] != "abc.marry.123":
            raise exceptions.AuthenticationFailed("用户信息校验失败")

        # 最后校验数据库是否存在此用户
        user = User.objects.filter(username="admin").first()

        if not user:
            raise exceptions.AuthenticationFailed("用户不存在")
        print(user)
        return (user, None)
