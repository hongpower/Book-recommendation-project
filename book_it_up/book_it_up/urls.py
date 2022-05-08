"""book_it_up URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import re_path
from haystack.views import SearchView, search_view_factory
from haystack.query import SearchQuerySet
from haystack.forms import ModelSearchForm

sqs = SearchQuerySet()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', include('login.urls')),
    path('/recommendation/', include('rcm.urls')),
    path('book_id/', views.get_info),
    path('mysite/',views.mysite, name='mysite'),
    path('mysite/mysite_likebook',views.mysite_likebook),
    path('mysite/mysite_wishlistbook',views.mysite_wishlistbook),
    path('mysite/all_like',views.all_like),
    path('mysite/all_wish',views.all_wish),
    path('mysite/user_info', views.user_info),
    path('mysite/mysite_update', views.mysite_update),
    path('mysite/all_like/mysite_likebook',views.mysite_likebook),
    path('mysite/all_wish/mysite_wishlistbook',views.mysite_wishlistbook),
    path('mysite/usage', views.usage),
    path('mysite/board', views.mysite_board),
    path('test/',views.test, name='test'),
    path('test/getbook',views.get_book),
    path('unlogged/', views.unlogged),
    path('modify_preference/', views.modify_preference),
    path('modify_wishlist/', views.modify_wishlist),
    re_path(r'^search/', include('haystack.urls')),
    path('auto_complete/', views.auto_complete, name='auto_complete'),
    #path('search/',SearchView(),  name='search'),
    path('profile/',views.profile),
    path('history_register/',views.history_register, name='history_register'),
    path('history_register/history', views.history),
    path('history_register/history_update', views.history_update, name='history_update'),
    path('history_register/history_delete', views.history_delete, name='history_delete')

]
