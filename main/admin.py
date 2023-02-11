from django.contrib import admin

from .models import Author, Review, Recipe, Comments

admin.site.register(Author)
admin.site.register(Review)
admin.site.register(Recipe)
admin.site.register(Comments)