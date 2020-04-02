import os
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'drinkslist_project.settings')

import django

django.setup()
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from drinkslist.models import UserProfile, Drink, Recipe


def populate():
    daiquiri_recipes = [
        {'Daiquiri':{'Equipment':'Coupette; Shaker; Hawthorn; Fine strainer; Jigger',
         'Ingredients':'Cuban Rum; Simple syrup; Lime juice; Ice',
         'HowTo':'Add 50ml Cuban Rum, 25ml lime juice and 15ml simple syrup to the shaker; Fill shaker with ice and coupette with ice and water; Shake vigorously for six seconds; Fine strain into coupette','username':'visitor1'}},
        {'Daiquiri':{'Equipment': 'Coupette; Shaker; Hawthorn; Fine strainer; Jigger',
         'Ingredients': 'Cuban Rum; Jamaican Rum; Simple syrup; Lime juice; Ice',
         'HowTo':'Add 35ml Cuban Rum, 15ml Jamaican Rum, 20ml lime juice and 10ml simple syrup.To the shaker; Fill shaker with ice and coupette with ice. And water; Shake vigorously for six seconds; Fine strain into coupette','username':'visitor2'}},
    ]

    toronto_recipes = [
        {'Toronto':{'Equipment': 'Nicanora; Mixing glass; Julep; Barspoon; Jigger',
         'Ingredients': 'Rye whiskey; Fernet Branca; Simple syrup; Orange Bitters; Ice',
         'HowTo': 'Add 50ml Rye, 10ml Fernet Branca, 10ml simple syrup to the mixing glass; Fill mixing glass with ice and nicanora with ice and water; Stir until optimal dilution; Strain into nicanora','username':'visitor2'}},
        {'Toronto':{'Equipment': 'Nicanora; Mixing glass; Julep; Barspoon; Jigger',
         'Ingredients': 'Rye whiskey; Fernet Branca; Simple syrup; Orange Bitters; Ice',
         'HowTo': 'something different','username':'visitor1'}}
    ]

    drinks = {'Daiquiri': {'recipes': daiquiri_recipes,'username':'visitor1'},
              'Toronto': {'recipes': toronto_recipes,'username':'visitor2'}}

    u = User.objects.get_by_natural_key('Luke1')
    users = {
        'visitor1':{'password':'visitor1',
        'email':'visitor1@gmail.com',
        'drinks':{'Daiquiri',}},
        
        'visitor2':{'password':'visitor2',
        'email':'visitor2@gmail.com',
        'drinks':{'Toronto',}
        }
    }

    for user in users:
        u = add_user(user, users[user]['password'], users[user]['email'])

    for d in drinks:
        added = None
        for u in User.objects.all():
            if drinks[d]['username'] == u.username:
                added = u
                add_drink(d,added)

    for drink in Drink.objects.all():
        added = None #username 
        drink_added = None # drink name 
        re = None #recipe name 
        for u in User.objects.all():
            if drink.name == 'Daiquiri':
                for r in daiquiri_recipes:
                    if u.username == r[drink.name]['username']:
                        added = u
                        drink_added = drink
                        add_recipe(drink_added,r[drink.name]['Equipment'],r[drink.name]['Ingredients'],r[drink.name]['HowTo'],added)
                        break
            elif drink.name == 'Toronto':
                for r in toronto_recipes:
                    if u.username == r[drink.name]['username']:
                        added = u
                        drink_added = drink
                        add_recipe(drink_added,r[drink.name]['Equipment'],r[drink.name]['Ingredients'],r[drink.name]['HowTo'],added)
                        break

        

    for d in Drink.objects.all():
        for r in Recipe.objects.filter(drink_name=d):
            print(f'- {d}: {r}')


def add_user(username,password,email):
    user = User.objects.create_user(username=username,email=email)
    user.set_password(password)
    user.save()
    u = UserProfile.objects.get_or_create(user=user)
    return user


def add_recipe(drink, equipment, ingredients, howto, user):
    r = Recipe.objects.get_or_create(drink_name=drink, added_by=user)[0]
    r.equipment = equipment
    r.ingredients = ingredients
    r.how_to = howto
    r.save()
    return r


def add_drink(name, user):
    d = Drink.objects.get_or_create(added_by=user)[0]
    d.name =name
    d.date_added = date.today()
    d.save()
    return d


if __name__ == '__main__':
    print('Starting Drinkslist population script...')
    populate()
