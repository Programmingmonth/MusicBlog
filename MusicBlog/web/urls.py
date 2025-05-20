from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('piano/', views.piano, name='piano'),
    path('composition/', views.composition, name='composition'),
    path('theory/', views.theory, name='theory'),
    path('about/', views.about, name='about'),  # About page
]