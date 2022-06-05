from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=100,blank=True)
    content = models.TextField()
    # date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(null=True, default=0)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default='',null='True',related_name='author')

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=30)
    pic = models.ImageField(upload_to='uploads/')
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,default='',null=True)

    # def __str__(self) -> str:
    #     return f'{self.user} Profile'
