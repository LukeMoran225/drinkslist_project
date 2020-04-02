from django.urls import path
from drinkslist import views
from drinkslist.views import AboutView,RegisterProfile,ProfileView,ListProfilesView

app_name = 'drinkslist'
LOGIN_URL = 'drinkslist:login'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contactus/',views.contactus,name='contactus'),
    # path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    path('check_login/', views.check_login, name='check_login'),#helper func
    path('user_delete/', views.user_delete, name='user_delete'),#helper func
    path('search/',views.search,name='search'),#helper func
    path('register_profile/', views.register_profile, name='register_profile'),
    path('recipe/',views.recipe_list, name='recipe_list'),
    path('drinks/', views.drinks, name='drinks'),
]
