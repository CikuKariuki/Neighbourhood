# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import Neighbourhood,Business,Profile

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Roasters = neighbourhood(neighbourhood = 'Roasters')

    def test_instance(self):
        self.assertTrue(isinstance(self.Roasters,neighbourhood))