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
        {'Equipment': 'Coupette; Shaker; Hawthorn; Fine strainer; Jigger',
         'Ingredients': 'Cuban Rum; Simple syrup; Lime juice; Ice',
         'HowTo': 'Add 50ml Cuban Rum, 25ml lime juice and 15ml simple syrup'
                  'to the shaker; Fill shaker with ice and coupette with ice'
                  'and water; Shake vigorously for six seconds; Fine strain '
                  'into coupette'},
        {'Equipment': 'Coupette; Shaker; Hawthorn; Fine strainer; Jigger',
         'Ingredients': 'Cuban Rum; Jamaican Rum; Simple syrup; Lime juice; Ice',
         'HowTo': 'Add 35ml Cuban Rum, 15ml Jamaican Rum, 20ml lime juice and 10ml simple syrup'
                  'to the shaker; Fill shaker with ice and coupette with ice'
                  'and water; Shake vigorously for six seconds; Fine strain '
                  'into coupette'}]

    toronto_recipes = [
        {'Equipment': 'Nicanora; Mixing glass; Julep; Barspoon; Jigger',
         'Ingredients': 'Rye whiskey; Fernet Branca; Simple syrup; Orange Bitters; Ice',
         'HowTo': 'Add 50ml Rye, 10ml Fernet Branca, 10ml simple syrup'
                  'to the mixing glass; Fill mixing glass with ice and nicanora with ice'
                  'and water; Stir until optimal dilution; Strain into nicanora'},
        {'Equipment': 'Nicanora; Mixing glass; Julep; Barspoon; Jigger',
         'Ingredients': 'Rye whiskey; Fernet Branca; Simple syrup; Orange Bitters; Ice',
         'HowTo': 'something different'}]

    drinks = {'Daiquiri': {'recipes': daiquiri_recipes},
              'Toronto': {'recipes': toronto_recipes}}

    u = User.objects.get_by_natural_key('Luke1')

    for drink, drink_data in drinks.items():
        d = add_drink(drink, u)
        for r in drink_data['recipes']:
            add_recipe(d, r['Equipment'], r['Ingredients'], r['HowTo'], u)

    for d in Drink.objects.all():
        for r in Recipe.objects.filter(drink_name=d):
            print(f'- {d}: {r}')


def add_recipe(drink, equipment, ingredients, howto, user):
    r = Recipe.objects.get_or_create(drink_name=drink, equipment=equipment,
                                     ingredients=ingredients, how_to=howto,
                                     added_by=user)[0]
    r.save()
    return r


def add_drink(name, user):
    d = Drink.objects.get_or_create(name=name, date_added=date.today(), added_by = user)[0]
    d.save()
    return d


if __name__ == '__main__':
    print('Starting Drinkslist population script...')
    populate()
