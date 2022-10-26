from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo'),
    path('about/', views.demo, name='demo')
]
