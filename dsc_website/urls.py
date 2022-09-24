
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dsc_app.urls')),
    path('accounts/',include('allauth.urls')),
]
