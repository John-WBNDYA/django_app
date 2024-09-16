from django.urls import path
from .views import MyLoginView
from .views import home
from . import views

urlpatterns = [
    # Url patterns for web pages 
    path('', MyLoginView.as_view(), name='login'),
    path('home/',home, name='home'),  
    path('about/', views.about, name='about'),
    path('albums/', views.albums, name='albums'),
]
