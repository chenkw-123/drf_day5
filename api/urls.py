from api import views

from django.urls import path
urlpatterns = [
    path("test/",views.TestAPIView.as_view()),
    path("is_auth/", views.TestPermissionAPIView.as_view()),
    path("user_login/", views.UserLoginOrReadOnly.as_view()),
    path("throttle/", views.SendMessageAPIView.as_view()),
]