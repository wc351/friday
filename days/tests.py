"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from .views import Monday


class UrlTests(TestCase):
    def test_monday_url(self):
        monday_page = resolve(reverse('days:monday'))
        return self.assertEqual(monday_page.func.__name__,
                                Monday.__name__)



class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
