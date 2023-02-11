import datetime
import email
from gc import get_objects
from msilib.schema import ListView
from unicodedata import name
from django.shortcuts import render, redirect
from .models import Review, Author, Recipe, Comments
from .forms import AddReview, AddRecipe, AddComments, UserRegisterForm
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    all_reviews = Review.objects.all().order_by('-issued')[:1]
    return render(request, 'main/home.html', {'reviews': all_reviews})

@permission_required('main.main_review')
def add_review(request):
    if request.method == "POST":
        new_form = AddReview(request.POST, request.FILES)
        
        if new_form.is_valid():
            review = new_form.save(commit=False)
            review.author = Author.objects.get(email=request.user.email)
            review.issued = datetime.datetime.now()
            review.save()
            new_form.save_m2m()

            return redirect('home')
            
    else:
        new_form = AddReview()

    return render(request, 'main/add_review.html', {'new_form': new_form})
         

def recipes(request):
    search_query = request.GET.get('search_recipe','')
    if search_query:
        all_recipes=Recipe.objects.filter(Q(title__icontains=search_query) | Q(products__icontains=search_query))
        if not all_recipes:
            return render(request, 'main/notfound.html')
            
    else:
        all_recipes = Recipe.objects.all().order_by('-time')
        
       

    return render(request, 'main/recipes.html', {'recipes': all_recipes})


def notfound(request):
    pass



def recipe(request, id):
    try:
        recipe = Recipe.objects.get(id=id)
        comment = Comments.objects.filter(recipe=recipe)

        if request.method == 'POST':
            form = AddComments(request.POST)
            if form.is_valid():
                com = form.save(commit=False)
                com.author = Author.objects.get(email=request.user.email)
                com.issued = datetime.datetime.now()
                com.recipe = recipe
                com.save()
                form.save_m2m()

            return redirect('recipes')
            
        else:
            form = AddComments()

    except:
        recipe = ""
    return render(request, 'main/recipe.html', {'recipe': recipe, 'form': form, 'comment': comment})



         
def add_recipe(request):
    
    if request.method == "POST":
        new_form = AddRecipe(request.POST, request.FILES)
        
        if new_form.is_valid():
            recipe = Recipe()
            recipe.the_author = Author.objects.get(email=request.user.email)
            recipe.title = new_form.cleaned_data['title']
            recipe.products = new_form.cleaned_data['products']
            recipe.cooking = new_form.cleaned_data['cooking']
            recipe.time = datetime.datetime.now()
            recipe.image = new_form.cleaned_data['image']
            recipe.save()

            return redirect('recipes')
            
    else:
        new_form = AddRecipe()

    return render(request, 'main/add.html', {'new_form': new_form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered')
            return redirect('register')
        else:
            messages.error(request, 'Registration error')
    else:
        form = UserRegisterForm()

    return render(request, 'main/register.html', {"form": form})