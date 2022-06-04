from distutils.command.upload import upload
from email.mime import image
from time import timezone
from unicodedata import name
from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=100,blank=True)
    content = models.TextField()
    # date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=30)
    pic = models.ImageField(upload_to='uploads')
    bio = models.TextField()

    # def __str__(self) -> str:
    #     return f'{self.user} Profile'
