from django.test import TestCase
from users.models import Blog

# Create your tests here.
class BlogTestCase(TestCase):
    def setUp(self):
        Blog.objects.Create(title="Test title 001", content="Test content 001")
        Blog.objects.Create(title="Test title 002", content="Test content 002")
        Blog.objects.Create(title="Test title 003", content="Test content 003")
        pass