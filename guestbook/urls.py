from django.urls import path 

#import all views your app have
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('sign/', views.sign, name='sign')
]