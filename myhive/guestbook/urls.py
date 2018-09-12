from django.urls import path
from . import views

urlpatterns = [
    path('', views.good_create, name='guestbook'),
]

