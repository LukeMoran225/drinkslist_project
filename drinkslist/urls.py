from django.urls import path
from drinkslist import views

app_name = 'drinkslist'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('contactus/',views.contactus,name='contactus'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('search/',views.search,name='search'),
]
