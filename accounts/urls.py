from django.urls import path

from .views import CreditProviderRegisterApi,CustomerRegisterApi,LoginApi

app_name = "accounts"


urlpatterns = [
    path('credit_provider_register/',CreditProviderRegisterApi.as_view(),name="creditproviderregister"),
    path('customer_register/',CustomerRegisterApi.as_view(),name="customer_register"),
    path('login/',LoginApi.as_view(),name="login")
]
