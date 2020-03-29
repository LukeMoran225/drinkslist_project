from django.urls import path
from drinkslist import views

app_name = 'drinkslist'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('contactus/',views.contactus,name='contactus'),
]