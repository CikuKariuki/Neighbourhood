# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import Neighbourhood,Business,Profile

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.neighbourhood = Neighbourhood(neighbourhood = 'Roasters')

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_save(self):
        self.neighbourhood.save_neighbourhood()
        neighbourhood = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhood)>0)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.neighbourhood = Neighbourhood(neighbourhood = 'Roasters')
        self.neighbourhood.save_neighbourhood()

        self.wanjiku = Profile(avatar = '/avatar/default.png',description = 'happy neighbour',neighbourhood = 'roasters',username = 'Ciku',name='Wanjiku',email='ciku@user.com')

    def test_save(self):
        self.wanjiku.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)


class BusinessTestClass(TestCase):
    def setUp(self):
        self.wanjiku = Profile(first_name = 'Wanjiku',last_name='Kariuki',username='ciku_k',email='sheekokariuki@gmail.com')
        self.wanjiku.save_profile()

        self.business = Business(name='Kuku Shop',email='kukushop@roasters.com',location = 'Roasters',user = self.wanjiku)

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_save(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(profiles)>0)

    def tearDown(self):
        Profile.objects.all.delete()
        Business.objects.all().delete()

class healthservicesTestClass(TestCase):
    def setUp(self):
        self.Radiotherapy = healthservices(healthservices='Radiotherapy')

    def test_instance(self):
        self.assertTrue(isinstance(self.Radiotherapy,healthservices))

    def tearDown(self):
        healthservices.objects.all().delete()

    def test_save_method(self):
        self.Radiotherapy.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health)>0)

    def test_delete_method(self):
        self.Radiotherapy.delete_healthservices('Radiotherapy')
        health = healthservices.objects.all()
        self.assertTrue(len(health)==0)
