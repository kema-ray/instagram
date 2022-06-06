from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from insta import views as user_views
from .views import *
# from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.home,name='home'),
    path('search/',views.search_results,name='search_results'),
    path('new_post/',views.new_post,name='new_post'),
    path('profile/', user_views.profile,name = 'profile'),
    path('user_profile/', user_views.user_profile, name='user_profile'),
    path('<str:pk>',views.likes, name='likes'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
