from django.contrib import admin
from django.urls import path, include
from MSMEOrderingWebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login_view, name='login'),
    path('MSMEOrderingWebApp/', include('MSMEOrderingWebApp.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
