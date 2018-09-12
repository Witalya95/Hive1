from django.urls import path
from .views import DefaultPageView

from . import views

urlpatterns = [
    path('', DefaultPageView.as_view(), name='default'),
]