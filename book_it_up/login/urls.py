from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('success/',views.success, name='success'),
    path('logout/',views.logout, name='logout'),
    path('id_chk/',views.id_chk, name='chk'),
    path('nickname_chk/',views.nickname_chk, name='nickname'),
    path('password_chk/',views.password_chk, name='password'),

]
