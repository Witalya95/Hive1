from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from . import views


urlpatterns = [

    path('', BlogListView.as_view(), name='blogs'),
    path('<int:blog_id>/', BlogDetailView.as_view(), name='blog'),
    path('add/', BlogCreateView.as_view(), name='blog_add'),
    path('update/<int:blog_id>', BlogUpdateView.as_view(), name='blog_update'),
    path('addcomment/<int:blog_id>', views.comment_create, name='addcomment'),
    path('delete/<int:blog_id>', BlogDeleteView.as_view(), name='blog_delete'),
]