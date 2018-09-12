from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from default.views import CategoryListMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


from .models import Category, Good

# Create your views here.

class GoodListView(ListView, CategoryListMixin):

    template_name = 'good/goods.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        if self.kwargs["cat_id"] == None:

            self.kwargs["cat_id"] = 1
        try:
            self.cat = Category.objects.get(pk=self.kwargs["cat_id"])
        except KeyError:
            self.cat = Category.objects.first()

        return super(GoodListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)
        context['category'] = self.cat
        return context

    def get_queryset(self):
        return Good.objects.filter(category=self.cat).order_by('name')


class GoodDetailView(DetailView, CategoryListMixin):
    template_name = 'good/good_detail.html'
    model = Good
    pk_url_kwarg = 'good_id'

    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        return context


class CategoryDeleteView(SuccessMessageMixin, DeleteView, CategoryListMixin):
    model = Category
    pk_url_kwarg = 'cat_id'
    success_url = reverse_lazy('default')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse_lazy('goods', kwargs={'cat_id' : 1}))
        else:
            messages.add_message(request, messages.SUCCESS, 'Категорію видалено')
            return super(CategoryDeleteView, self).post(request, *args, **kwargs)


class CategoryCreateView(SuccessMessageMixin, CreateView, CategoryListMixin):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('default')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse_lazy('default'))
        else:
            messages.add_message(request, messages.SUCCESS, 'Категорію додано')
            return super(CategoryCreateView, self).post(request, *args, **kwargs)


class GoodCreateView(SuccessMessageMixin, CreateView, CategoryListMixin):
    model = Good
    fields = ['name', 'description', 'content', 'photo', 'category']
    success_url = reverse_lazy('default')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse_lazy('default'))
        else:
            messages.add_message(request, messages.SUCCESS, 'Товар додано')
            return super(GoodCreateView, self).post(request, *args, **kwargs)


class GoodUpdateView(UpdateView, CategoryListMixin):
    model = Good
    fields = ['name', 'description', 'content', 'photo', 'category']