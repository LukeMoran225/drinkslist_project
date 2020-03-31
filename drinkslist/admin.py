from django.contrib import admin
from drinkslist.models import UserProfile, Drink, Recipe
from drinkslist.models import Followed, Comment, Rating


class DrinkAdmin(admin.ModelAdmin):
    # customising the Drink page
    list_display = ('name', 'date_added','added_by')

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('drink_name','added_by','equipment','ingredients','how_to','picture')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('made_by','date_added','for_recipe','comment')

class FollowedAdmin(admin.ModelAdmin):
    list_display = ('followed_name','follower_name')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('made_by','for_recipe','rating')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','is_professional','picture')


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Drink,DrinkAdmin)
admin.site.register(Recipe,RecipeAdmin)
admin.site.register(Followed,FollowedAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Rating,RatingAdmin)

