from dataclasses import fields
from unicodedata import name
from django import forms
from .models import Review, Recipe, Comments, Author
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)

class AddRecipe(forms.Form):
    title = forms.CharField(max_length=100)
    products = forms.CharField(widget=forms.Textarea())
    cooking = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField()

class AddComments(forms.ModelForm):
    content = forms.CharField(label='Content', widget=forms.Textarea())
    class Meta:
        model = Comments
        fields = ('content',)



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
