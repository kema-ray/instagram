
from django.test import TestCase
from .models import *
# from django.contrib.auth.models import User

# Create your tests here.
class TestPost(TestCase):
    def setUp(self):
        self.walking = Profile(title='walking',image= 'image.jpg',user="User")
        self.walking.save()

        # self.image_test=Post(image='default.png',name='test',content='default test',user=self.profile_test)

    def test_instance(self):
        self.assertTrue(isinstance(self.walking, Post))