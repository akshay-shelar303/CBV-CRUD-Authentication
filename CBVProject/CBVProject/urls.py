from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('laptop/',include('LaptopApp.urls')),
    path('accounts/',include('AccountsApp.urls')),
]
