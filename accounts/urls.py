from django.urls import path

from .views import LoginApi,UserRegisterApi

app_name = "accounts"


urlpatterns = [
    path('register/',UserRegisterApi.as_view(),name="creditproviderregister"),
    path('login/',LoginApi.as_view(),name="login")
]
