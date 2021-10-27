from django.contrib import admin
from django.urls import path
from .import views

app_name = 'artcraft'

urlpatterns = [
    path('index/', views.homeView.as_view(), name="home"),
    path('dashboard/', views.dashboardView.as_view(), name="dashboard"),
    path('login/', views.loginView.as_view(), name="login"), 
    path('register/', views.registerView.as_view(), name="register"),
    path('registerArtist/', views.registerArtistView.as_view(), name="registerArtist"),
    path('about/', views.aboutView.as_view(), name="about"),
    path('artwork/', views.artworkView.as_view(), name="artwork"),
    path('contact/', views.contactView.as_view(), name="contact"),
]