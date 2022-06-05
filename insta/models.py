from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=100,blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(null=True, default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='',null='True',related_name='author')

    @classmethod
    def all_posts(cls):
        posts = cls.objects.all()
        return posts

    def save_post(self):
        self.save()

    @classmethod
    def search_by_title(cls,search_term):
        profiles=cls.objects.filter(title__icontains=search_term)
        return profiles

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=30)
    pic = models.ImageField(upload_to='uploads/')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,default='',null=True)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'
