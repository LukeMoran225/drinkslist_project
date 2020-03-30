from django.contrib import admin
from drinkslist.models import UserProfile, Drink, Recipe
from drinkslist.models import Followed, Comment, Rating

admin.site.register(UserProfile)
admin.site.register(Drink)
admin.site.register(Recipe)
admin.site.register(Followed)
admin.site.register(Comment)
admin.site.register(Rating)

