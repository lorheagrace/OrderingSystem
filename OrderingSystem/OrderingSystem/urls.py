from django.contrib import admin
from django.urls import path, include
from MSMEOrderingWebApp import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('MSMEOrderingWebApp/', include('MSMEOrderingWebApp.urls')),
    path('admin/', admin.site.urls),
]
