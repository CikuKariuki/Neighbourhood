from django import forms
from .models import notifications,Business,Profile,BlogPost,Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','neighbourhood']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']
