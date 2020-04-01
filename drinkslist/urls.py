from django.urls import path
from drinkslist import views
from drinkslist.views import AboutView

app_name = 'drinkslist'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contactus/',views.contactus,name='contactus'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('search/',views.search,name='search'),
    path('logout/',views.user_logout,name='logout'),
]
