from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('sinup/', views.sinup, name='sinup'),
    path('logout/', views.logout, name='logout'),
    path('post/', views.post, name='post'),
    path('', views.all, name='all'),
    path('all/<slug:slug>/', views.detail, name='detail'),
]
