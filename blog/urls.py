from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewAllPost, name='blog'),
    path('<int:post_id>/', views.viewPost, name="post"),
    path('author/<int:post_author>/', views.sortByAuthor, name="sort_author"),
    # path('<str:date>/', views.sortByDate, name="sort_date")
]
