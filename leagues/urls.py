from django.urls import path
from . import views

urlpatterns = [
	
	path('',views.home,name="home"),
	path('', views.make_data, name="make_data"),
    path('leagues/Sports_1', views.index),
    path('leagues/Sports_2', views.index_2),
	
]
