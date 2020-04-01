from django.test import TestCase
from drinkslist.models import Drink, Recipe, User, UserProfile
import datetime
from django.utils import timezone
from datetime import date
from django.urls import reverse
from drinkslist.forms import UserForm, UserProfileForm

""" 
Unit test for models
"""

class DrinkMethodTests(TestCase):

    def setUp(self):
        
        admin = User.objects.create(username="admin",email="admin@gmail.com")
        UserProfile.objects.create(user=admin)
        visitor = User.objects.create()

        Drink.objects.create(name="test1",date_added=date.today()-datetime.timedelta(days=1),added_by=admin)

        Drink.objects.create(name="test2",date_added=date.today()+datetime.timedelta(days=1),added_by=visitor)

    def test_date_added_recently(self):
        """
         false when date is over
        """
        today = date.today()
        drink = Drink.objects.get(name="test1")
        self.assertEqual((today>drink.date_added ), True)

class RecipeMethodsTests(TestCase):

    def setUp(self):
        admin = User.objects.create(username="admin",email="admin@gmail.com")
        UserProfile.objects.create(user=admin)
        visitor = User.objects.create()
        
        drink = Drink.objects.create(name="test1",date_added=date.today()-datetime.timedelta(days=1),added_by=admin)

        Recipe.objects.create(drink_name=drink,added_by=visitor,equipment="",ingredients="",how_to="")
        
        Recipe.objects.create(drink_name=drink,added_by=admin,equipment="1",ingredients="2",how_to="3")

    def test_empty_recipe(self):
        visitor = User.objects.get(username="")
        admin = User.objects.get(username="admin")
        drink = Drink.objects.get(name="test1")
        recipe = Recipe.objects.get(drink_name=drink,added_by=admin)
        recipe2 = Recipe.objects.get(drink_name=drink,added_by=visitor)

        self.assertEqual(recipe.equipment=="",False)
        self.assertEqual(recipe.ingredients=="",False)
        self.assertEqual(recipe.how_to=="",False)

    def test_equipment_max_length(self):
        pass

    def test_ingredients_max_length(self):
        pass
    
    def test_how_to_max_length(self):
        pass


"""
Unit test for views mocking
"""

class RegisterViewTests(TestCase):
    def test_register_view_not_login(self):
        """
        GET HttpRequest - not login

        should display "Registered" & no forms
        """
        response = self.client.get(reverse('drinkslist:register'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['registered'],False)

class LoginViewTests(TestCase):

    def test_login_view_get(self):
        response = self.client.get(reverse('drinkslist:login'))
        self.assertEqual(response.status_code, 200)

# class SearchViewTests(TestCase):
#     def test_search(self):
#         selection = "google"
#         query = "test"
#         response = self.client.post(reverse('drinkslist:search'),{'search-selection':selection,'query':query})

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response,True )
