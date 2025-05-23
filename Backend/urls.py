from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
  return HttpResponse("Welcome to my Django app!")


urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
      ]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)