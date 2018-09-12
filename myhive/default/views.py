from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import ContextMixin, TemplateView
from news.models import News
from guestbook.models import Guestbook
from good.models import Category

# Create your views here.


class CategoryListMixin(ContextMixin):
    def get_context_data(self, **kwargs):

        context = super(CategoryListMixin, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.order_by("name")
        context["current_url"] = self.request.path

        return context


class DefaultPageView(TemplateView, CategoryListMixin):

    template_name = "default/defaultpage.html"
    news = News.objects.all()[0:3]
    coments = Guestbook.objects.all()[0:3]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DefaultPageView, self).get_context_data(**kwargs)
        context['news'] = self.news
        context['coments'] = self.coments
        return context



