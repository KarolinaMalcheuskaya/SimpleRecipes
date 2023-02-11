from distutils.command.upload import upload
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False, primary_key=True)


class Review(models.Model):
    content = models.TextField()
    issued = models.DateTimeField()
    
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    products = models.TextField()
    cooking = models.TextField()
    time = models.DateTimeField()
    image = models.ImageField(upload_to='uploads')

    the_author = models.ForeignKey('Author', on_delete=models.CASCADE)


class Comments(models.Model):
    content = models.TextField()
    issued = models.DateTimeField()

    recipe = models.ForeignKey('Recipe', related_name='comments_recipe', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)


