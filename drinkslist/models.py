from django.db import models
from django.contrib.auth.models import User
from datetime import date

from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_professional = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Drink(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_added = models.DateField(default=date.today)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Drink, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    # ID static variable that increments by 1
    # ID = models.IntegerField(primary_key=True)
    drink_name = models.ForeignKey(Drink, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.CharField(max_length=250)
    ingredients = models.CharField(max_length=250)
    how_to = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='recipe_images', blank=True)

    def __str__(self):
        return str(self.drink_name) + '' + str(self.id)


class Followed(models.Model):
    followed_name = models.CharField(max_length=100)
    follower_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Followers'

    def __str__(self):
        return self.followed_name


class Comment(models.Model):
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(default=date.today)
    for_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)

    def __str__(self):
        return self.comment


class Rating(models.Model):
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    for_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return self.for_recipe
