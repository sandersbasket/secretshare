from django.urls import path

from . import views

urlpatterns = [
    path('paste/new/', views.paste_create, name='paste_create'),
    path('paste/<slug:slug>/', views.paste_detail, name='paste_detail'),
    path('', views.paste_list, name='paste_list'),
]