from django import forms
from django.contrib.auth.models import User
from django.http import request
from drinkslist.models import Recipe, UserProfile, Drink


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('is_professional', 'is_private', 'picture')


class RecipeCreateForm(forms.ModelForm):
    # added_by = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Recipe
        fields = (
            'drink_name',
            # 'added_by',
            'equipment',
            'ingredients',
            'how_to',
            'picture',
        )


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = (
            'name',
        )
