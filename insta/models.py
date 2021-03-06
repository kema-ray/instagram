
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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

    def save_profile(self):
        self.user

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self) -> str:
        return f'{self.user.username} Profile'

class Follow(models.Model):
    follower = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='following')
    followed = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='folowers')

    def __str__(self):
        return f'{self.follower} Follow'

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="comments")
    created = models.DateTimeField(auto_now_add=True,null=True)

    @classmethod
    def delete_comment(cls,id):
        comment = Comment.objects.get(id=id)
        comment.delete()
        
    def __str__(self):
        return f'{self.user.name} Post'
