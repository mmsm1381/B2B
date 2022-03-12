from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manager/',include("business_manager.urls",namespace="business_manager")),
    path('accounts/',include("accounts.urls",namespace="accounts"))
]
