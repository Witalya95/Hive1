from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [

    path('', NewsListView.as_view(), name='news'),
    path('<int:news_id>/', NewsDetailView.as_view(), name='news_detail'),
    path('add/', NewsCreateView.as_view(), name='news_add'),
    path('update/<int:news_id>', NewsUpdateView.as_view(), name='news_update'),
    path('delete/<int:news_id>', NewsDeleteView.as_view(), name='news_delete'),
]