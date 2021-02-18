from . import views
from django.urls import path

urlpatterns = [
    path('id', views.ReturnId.as_view()),
    path('userinfo', views.ReturnUserInfo.as_view())
]