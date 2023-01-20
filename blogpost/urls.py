from django.urls import path
from blogpost import views

urlpatterns = [
    path('blogposts/', views.BlogPostList.as_view()),
    path('blogposts/<int:pk>/', views.BlogPostDetail.as_view()),
]
