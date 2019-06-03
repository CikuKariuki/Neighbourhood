# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import ProfileForm,BusinessForm,CommentForm
from django.contrib.auth.decorators import login_required

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
def profile(request, username):
    profile = User.objects.get(username=username)

    try:
        profile_details = Profile.get_by_id(profile.id)
    
    except:
        profile_details = Profile.filter_by_id(profile.id)
      

    posts = Posts.get_profile_posts(profile.id) 

    context = {
        "profile":profile,
        "profile_details":profile_details,
        "posts":posts,
    }

    return render(request,'profile.html',context)