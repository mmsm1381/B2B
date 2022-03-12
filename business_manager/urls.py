from django.urls import path

from .views import TransactionAPI

app_name = "business_manager"


urlpatterns = [
    path('transactions/',TransactionAPI.as_view(),name="transactions"),
]
