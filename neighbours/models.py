# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    location = models.CharField(max_length = 150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name()

    def save_business(self):
        self.save()

    @classmethod
    def search_by_business(cls,search_term):
        business = cls.objects.filter(business_icontains=search_term)
        return business


class Neighbourhood(models.Model):
    neighbourhood = models.CharField(max_length = 150)

    def __str__(self):
        return self.neighbourhood

    def save_neighbourhood(self):
        self.save()

    
class Profile(models.Model):
    avatar = models.ImageField(upload_to = 'avatars/')
    description = models.TextField()
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    email = models.EmailField()

    def __str__(self):
        return self.name


    def save_profile(self):
        self.save()

    