from django.contrib import admin
from django.urls import path
from sampleApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/moto/',views.sayhello),
    path('HelloTemplate/',views.templateHello),
    path('insert/',views.insert),
  
]
