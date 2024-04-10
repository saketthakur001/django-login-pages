from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('help_', views.help_, name='help_'),
    path('', views.Home, name='Home')
]