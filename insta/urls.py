from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from insta import views as user_views

urlpatterns=[
    path('',views.home,name='home'),
    path('search/',views.search_results,name='search_results'),
     path('profile/', user_views.profile,name = 'profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
