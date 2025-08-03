from django.urls import path
from . import views

urlpatterns = [
    path('search/',views.search_articles,name='search'),
    path('authors/',views.author,name='author'),
    path('authors/<str:username>/',views.author_list,name='author_list'),
    path('author/<int:id>/<slug:slug>/',views.author_detail,name='author_detail'),
    path('<slug:slug>/',views.post_detail,name='detail'),
    path('',views.post_lists,name='list'),
]
