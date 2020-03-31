# from django.db import models


# # User class will be implemented with the password package
# class Drink(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     date_added = models.DateField()
#     # addedby will become foreign key to user
#     added_by = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Recipe(models.Model):
#     # ID static variable that increments by 1
#     # Recipe needs to be linked to Drink directly
#     ID = models.IntegerField(unique=True)
#     drink_name = models.ForeignKey(Drink.name, on_delete=models.CASCADE)
#     added_by = models.ForeignKey(Drink.added_by, on_delete=models.CASCADE)
#     equipment = models.CharField(max_length=250)
#     ingredients = models.CharField(max_length=250)
#     how_to = models.CharField(max_length=250)

#     # Also an image field

#     def __str__(self):
#         return self.drink_name + self.ID


# class Followed(models.Model):
#     # Both will be foreign keys to User
#     followed_name = models.CharField(max_length=100)
#     follower_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.followed_name + self.follower_name


# class Comment(models.Model):
#     # made_by foreign key to user
#     made_by = models.CharField(max_length=100)
#     date_added = models.DateField()
#     for_recipe = models.ForeignKey(Recipe.ID, on_delete=models.CASCADE)
#     comment = models.CharField(max_length=250)

#     def __str__(self):
#         return self.made_by + self.for_recipe


# class Rating(models.Model):
#     # made_by foreign key to user
#     made_by = models.CharField(max_length=100)
#     for_recipe = models.ForeignKey(Recipe.ID, on_delete=models.CASCADE)
#     rating = models.IntegerField()

#     def __str__(self):
#         return self.for_recipe + self.made_by
