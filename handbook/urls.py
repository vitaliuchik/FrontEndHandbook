from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('text/', views.text, name='text'),
    path('tables/', views.tables, name='tables'),
    path('forms/', views.forms, name='forms'),
    path('images/', views.images, name='images'),
    path('media/', views.media, name='media'),
    path('svg/', views.svg, name='svg'),
    path('animation/', views.animation, name='animation'),
    path('contact/', views.contact, name='contact'),
]