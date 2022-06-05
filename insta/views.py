from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required(login_url='/accounts/login/')
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

def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST,instance=request.user)
        profile_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user)

        if profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('home')

    else:
            profile_form = UpdateProfileForm(instance=request.user)
            user_form = UpdateUserForm(instance=request.user)

            param = {
                'user_form':user_form,
                'profile_form':profile_form,
            }

    return render(request,'profile.html', param)

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})
