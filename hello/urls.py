from django.urls import path
from . import views 

urlpatterns = [
   path('davis/', views.index, name='index')
]
