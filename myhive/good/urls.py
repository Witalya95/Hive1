from django.urls import path
from .views import GoodListView, GoodDetailView, CategoryCreateView, GoodCreateView, CategoryDeleteView


urlpatterns = [

    path('<int:cat_id>/', GoodListView.as_view(), name='goods'),
    path('good/<int:good_id>/', GoodDetailView.as_view(), name='good_detail'),
    path('add/', CategoryCreateView.as_view(), name='category_add'),
    path('delete/<int:cat_id>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('good/add/', GoodCreateView.as_view(), name='good_add'),
]