from unicodedata import name
from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class TestUser(TestCase):
    def setUp(self):
        self.rachel = User(username='ray',email='test@gmail.com',password='test123')
        self.rachel.save()

    def test_user_instance(self):
        self.assertTrue(isinstance(self.rachel,User))

class TestProfile(TestCase):
    def setUp(self):
        self.rachel = User(username='ray',email='test@gmail.com',password='test123')
        self.rachel.save()

        self.e_profile = Profile(user=self.rachel,pic = "../uploads/img.png",name="ray",bio="hello world")

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.e_profile,Profile))
class TestPost(TestCase):
    def setUp(self):
        self.e_profile = Profile(pic = "../uploads/img.png",name="ray",bio="hello world")
        self.e_profile.save()

        self.e_post = Post(image = "../uploads/img.png",title = "hello world",content="first program",likes = 10,date_posted= "June 5, 2022, 12:19 p.m.")

    def tearDown(self):
        Profile.objects.all().delete()
        Post.objects.all().delete()
    
    def test_post_instance(self):
        self.assertTrue(isinstance(self.e_post,Post))

class TestComment(TestCase):
    def setUp(self):
        self.rachel = User(username='ray',email='test@gmail.com',password='test123')
        self.rachel.save()

        self.e_profile = Profile(pic = "../uploads/img.png",name="ray",bio="hello world")
        self.e_profile.save()

        self.e_post = Post(image = "../uploads/img.png",title = "hello world",content="first program",likes = 10,date_posted= "2022-06-04 12:19")
        self.e_post.save()

        self.e_comment = Comment(comment =self.e_profile, created ="2022-06-04 12:19",post = self.e_post)

    def tearDown(self):
        Profile.objects.all().delete()
        Post.objects.all().delete()
        User.objects.all().delete()
    
    def test_comment_instance(self):
        self.assertTrue(isinstance(self.e_comment, Comment))



