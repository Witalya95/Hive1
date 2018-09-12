from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic.base import TemplateView
from default.views import CategoryListMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.


class ProfileTemplateView(TemplateView, CategoryListMixin):

    template_name = 'users/profile.html'

class ProfileUpdateView(UpdateView, CategoryListMixin):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    pk_url_kwarg = 'user_id'
    success_url = reverse_lazy('profile')