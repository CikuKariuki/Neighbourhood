# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import ProfileForm,BusinessForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Business,Neighbourhood,Profile,Comment
from django.contrib.auth.models import User

def index(request):
    return render(request,'hood.html')

def search_results(request):
    if 'business' in request.GET and request.GET['business']:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_business(search_term)

        message = f'{search_term}'

        return render(request,'search.html',{"message":message,"business":searched_business})

    else:
        message = "Invalid input"
        return render(request, 'search.html',{"message":message,"business":searched_business})

        
@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:

        form = ProfileForm()
    return render(request,'profile_form.html',{"form":form})

@login_required(login_url='/accounts/login/')
def profile(request,username):
    user = User.objects.get(username=username)
    profile =Profile.objects.get(username=user)

    return render(request,'profile.html',{"profile":profile})

def single_hood(request,location):
 
    location = Neighbourhood.objects.get(name=location) 
    print(location.location)
    businesses = Business.get_location_businesses(location.id) 
    posts = Posts.get_location_posts(location.id)
    
    business_form = BusinessForm(request.POST)
    if request.method == 'POST':
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.user = request.user
            business.location = location
            business.save()
        return redirect('single_hood',location)
    
    else:
        business_form = BusinessForm()
        
    
    posts_form = PostsForm(request.POST)
    if request.method == 'POST':
        if posts_form.is_valid():
            posts = posts_form.save(commit=False)
            posts.user = request.user
            posts.location = location
            posts.save()
        return redirect('single_hood',location)
    
    else:
        posts_form = BusinessForm()  
        
    context = {"location":location,
               "businesses":businesses,
               'business_form':business_form,
               "posts_form":posts_form,
                "posts":posts
                }
    
    
    return render(request,'hood.html',context)

