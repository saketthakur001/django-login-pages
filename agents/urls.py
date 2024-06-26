from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('help/', views.help_, name='help_'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home', views.home, name='home')
]
