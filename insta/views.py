from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    # title = 'Instagram'
    posts = Post.all_posts()
    s_posts = []
    for post in posts:
        picture = Profile.objects.filter(user=post.user.id).first()
        if picture:
            picture=picture.pic.url
        else:
            picture = ''
        obj = dict(
            author = post.user.username,
            avatar = picture,
            image = post.image.url,
            name = post.title,
            content = post.content
        )
        s_posts.append(obj)

    return render(request,'index.html',{"posts":s_posts})

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})
