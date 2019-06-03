# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse


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

        