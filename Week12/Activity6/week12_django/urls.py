
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def welcome(request, name):
    html = f"""
        <!doctype html>
        <html>
          <head>
            <meta charset='utf-8' />
            <title>Welcome</title>
            <link rel='stylesheet' href='/static/styles.css'>
          </head>
          <body>
            <h1>Welcome {name} to Django!</h1>
          </body>
        </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/<str:name>/', welcome, name='welcome'),
]
