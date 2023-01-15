from django.db import models

# Create your models here.

class Recipedb(models.Model):
    recipe_name = models.CharField(max_length=30),
    recipe_image = models.ImageField(upload_to='SampleImage', default='null.jpg'),
    instruction = models.TextField(),
    ingredients = models.TextField

def __str__(self):
    return self.name