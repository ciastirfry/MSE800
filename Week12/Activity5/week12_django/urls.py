
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def welcome(request, name):
    return HttpResponse(f"<h1>Welcome {name} to Django!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/<str:name>/', welcome, name='welcome'),
]
