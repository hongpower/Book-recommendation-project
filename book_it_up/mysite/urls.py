from django.urls import path
from . import views

urlpatterns = [

    path('',views.mysite, name='mysite'),
    path('mysite_likebook/',views.mysite_likebook),
    path('mysite_wishlistbook/',views.mysite_wishlistbook),
    path('all_like/',views.all_like),
    path('all_wish/',views.all_wish),
    path('user_info/', views.user_info),
    path('mysite_update/', views.mysite_update),
    path('all_like/mysite_likebook/',views.mysite_likebook),
    path('all_wish/mysite_wishlistbook/',views.mysite_wishlistbook),
    path('usage/', views.usage),
    path('board/', views.mysite_board)
]