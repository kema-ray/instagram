from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse
from dataclasses import fields


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    # title = 'Instagram'
    posts = Post.all_posts()
    s_posts = []
    for post in posts:
        picture = Profile.objects.filter(user=post.user.id).first()
        if picture:
            picture=picture.pic
        else:
            picture = ''
        obj = dict(
            author = post.user.username,
            avatar = picture,
            image = post.image.url,
            name = post.title,
            content = post.content,
            date_posted = post.date_posted,
            likes = post.likes
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

            context = {
                'user_form':user_form,
                'profile_form':profile_form,
            }

    return render(request,'profile.html', context=context)

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})


def user_profile(request,username):
    user_prof = get_object_or_404(User,username=username)
    if request.user == user_prof:
        return redirect('user_profile',username=request.user.username)
    user_posts = user_prof.profile.posts.all()

    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False

    context = {
        'user_prof':user_prof,
        'user_posts':user_posts,
        'followers':followers,
        'follow_status':follow_status,
    } 
    print(followers)
    return render(request,'user_profile.html',context=context)           

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            s_image = form.save(commit=False)
            s_image.user = current_user

            s_image.save()
        return redirect('home')
    else:
        form = NewPostForm()
    return render(request,'new_post.html',{"form":form})

def likes(request,pk):
    # post=get_object_or_404(Post, id=pk)
    post = Post.objects.get(pk=pk)
    post.likes+=1
    post.save()
    return redirect('home')

