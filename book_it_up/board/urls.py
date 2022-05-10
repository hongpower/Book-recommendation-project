from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='board'),
    path('detail/<str:board_id>',views.detail,name='detail'),
    path('insertform/',views.insert_form, name='inserform'), #insertform/ 요청받으면 views의 insert_form으로 가주세요
    path('booknote_search/<str:book_id>',views.booknote_search), #insertform/ 요청받으면 views의 insert_form으로 가주세요
    path('insertres/',views.insert_res),
    path('book_note/',views.booknote),
    path('detail/delete/<int:board_id>',views.delete),
    path('detail/update/<int:board_id>',views.update),

]
