from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from drinkslist.forms import RecipeCreateForm, UserForm, UserProfileForm
from drinkslist.google_search import run_google_search
from django.views import View
import json
from django.contrib.auth.models import User
from drinkslist.models import Recipe, UserProfile, Drink



def index(request):
    context_dict = {}
    return render(request, 'drinkslist/index.html',context_dict)

class AboutView(View):
    def get(self,request):
        return render(request,'drinkslist/about.html')

def contactus(request):
    return render(request,'drinkslist/contactus.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

                profile.save()

                registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'registration/registration_form.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('drinkslist:index'))
            else:
                return HttpResponse("Your Drinkslist account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'drinkslist/login.html')


def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
    if form.is_valid():
        user_profile = form.save(commit=False)
        user_profile.user = request.user
        user_profile.save()
        return redirect(reverse('drinkslist:index'))
    else:
        print(form.errors)

    context_dict = {'form': form}
    return render(request, 'drinkslist/profile_registration.html', context_dict)


class RegisterProfile(View):
    @method_decorator(login_required)
    def post(self,request):
        context_dict = {}
        form = UserProfileForm()
        form = UserProfileForm(request.POST, request.FILES)
        # check whether all the form fields are filled correctly
        if form.is_valid():
            # give the time to manipulate the new instance before commiting
            user_profile = form.save(commit=False)
            # refresh current user
            user_profile.user = request.user
            user_profile.save()
            return redirect(reverse('drinkslist:index'))
        else:
            print(form.errors)

        context_dict = {'form':form}
        return render(request, 'drinkslist/profile_registration.html', context_dict)
    
    @method_decorator(login_required)
    def get(self,request):
        form = UserProfileForm()
        context_dict = {'form':form}
        return render(request, 'drinkslist/profile_registration.html', context_dict)



class ProfileView(View):
   
    # avoid repeating [DRY]
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        # current seleted detailed form
        form = UserProfileForm({'is_professional': user_profile.is_professional,'is_private':user_profile.is_private,'picture': user_profile.picture})
        return (user, user_profile, form)

    @method_decorator(login_required)
    def get(self, request, username):
        # username from url, paramised view
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('drinkslist:index'))
        context_dict = {'user_profile': user_profile,
        'selected_user': user,
        'form': form}
        return render(request, 'drinkslist/profile.html', context_dict)
    
    # update profile
    @method_decorator(login_required)
    def post(self, request, username):
         # username from url, paramised view
        context_dict = {}
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            print("error")
            return redirect(reverse('drinkslist:index'))
        
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            # refresh the form and commit 
            form.save(commit=True)
            return redirect('drinkslist:profile', user.username)
        else:
            print(form.errors)
            # return old details
            context_dict = {'user_profile': user_profile,
            'selected_user': user,
            'form': form}
            return render(request, 'drinkslist/profile.html', context_dict)

class ListProfilesView(View):
    @method_decorator(login_required)
    def get(self,request):
        profiles = UserProfile.objects.filter(is_private=False)

        return render(request,'drinkslist/list_profiles.html',{'user_profile_list':profiles})

"""
AJAX HELPER FUNCTION
"""

# AJAX Applied - search helper function : return the searching results of google & Site
def search(request):
    result_list = []
    query = ""
    if request.method == 'POST':
        # search engine selection
        selection = request.POST['search-selection']
        # user query string
        query = request.POST['query'].strip()
        if query:
            if selection == "static":
                # default site static searching
                pass
            else:
                result_list = run_google_search(query)

    return HttpResponse(json.dumps(result_list))

# Ajax Applied - test user input in login page
def check_login(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('drinkslist:index'))
            else:
                return HttpResponse("Your Drinkslist account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied")

@login_required
def user_delete(request):
    if request.method == 'POST':
        id= int(request.POST.get('id'))
        user = User.objects.get(id=id)
        if user:
            user.delete()
            return HttpResponse("Deleted Successfully!")
    else:
            return HttpResponse("Access Fobbidden")


def show_drink(request, drink_name_slug):
    context_dict = {}

    try:
        drink = Drink.objects.get(slug=drink_name_slug)
        recipes = Recipe.objects.filter(drink_name=drink)
        context_dict['recipes'] = recipes
        context_dict['drink'] = drink
    except Drink.DoesNotExist:
        context_dict['drink'] = None
        context_dict['pages'] = None
    return render(request,'drinkslist/drink.html', context=context_dict)


def drinks(request):
    drink_list = Drink.objects.order_by('name')
    context_dict = {
        'drinks': drink_list,
    }
    return render(request,'drinkslist/drinks.html', context = context_dict)


def create_recipe(request):
    if request.method == 'POST':
        form =RecipeCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.added_by = request.user
            post.save()
    else:
        form = RecipeCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'drinkslist/create_recipe.html', context)

def  recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {
        'Recipe':recipe,
    }
    return render(request, 'drinkslist/recipe_detail.html', context)