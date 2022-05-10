from django.urls import path
from . import views

urlpatterns = [
    path('', views.rcm, name="rcm"),
    path('keyword', views.get_topic, name="keyword"),
    path('get_topic_rcm', views.get_topic_rcm)
]
