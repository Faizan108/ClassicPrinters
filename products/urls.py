from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all,name='all'),
    path('vis_card', views.visc,name='vis_cards'),
    path('letter_heads', views.leth,name='letter_heads'),
    path('brochure', views.bro,name='brochure'),
    path('envelope', views.env,name='envelope'),
]