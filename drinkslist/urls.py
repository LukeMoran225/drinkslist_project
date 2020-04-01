from django.urls import path
from drinkslist import views
from drinkslist.views import AboutView,RegisterProfile

app_name = 'drinkslist'
LOGIN_URL = 'drinkslist:login'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contactus/',views.contactus,name='contactus'),
    # path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('check_login/', views.check_login, name='check_login'),
    path('search/',views.search,name='search'),
    path('register_profile/', views.register_profile, name='register_profile'),
]
