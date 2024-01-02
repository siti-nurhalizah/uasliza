from django.contrib import admin
from django.urls import path
from webatik import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('cameras/', views.cameras),
    path('contact/', views.contact),
]
