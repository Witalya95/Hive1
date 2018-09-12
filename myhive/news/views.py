
from django.views.generic.dates import ArchiveIndexView
from .models import News
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from default.views import CategoryListMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class NewsListView(ArchiveIndexView, CategoryListMixin):
    model = News
    date_field = 'posted'
    template_name = 'news/news_index.html'
    paginate_by = 2
    allow_empty = True
    allow_future = True




class NewsDetailView(DetailView, CategoryListMixin):
    model = News
    template_name = 'news/news.html'
    pk_url_kwarg = 'news_id'


class NewsCreateView(SuccessMessageMixin, CreateView, CategoryListMixin):
    model = News
    fields = ['title', 'description', 'content']
    success_url = reverse_lazy('news')
    success_message = 'Новину додано'


class NewsUpdateView(SuccessMessageMixin, UpdateView, CategoryListMixin):
    model = News
    fields = ['title', 'description', 'content']
    pk_url_kwarg = 'news_id'
    success_url = reverse_lazy('news')
    success_message = 'Новину змінено'


class NewsDeleteView(SuccessMessageMixin, DeleteView, CategoryListMixin):
    model = News
    pk_url_kwarg = 'news_id'
    success_url = reverse_lazy('news')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.add_message(request, messages.SUCCESS, 'Видалення скасовано')
            return HttpResponseRedirect(reverse_lazy('news'))
        else:
            messages.add_message(request, messages.SUCCESS, 'Новину видалено')
            return super(NewsDeleteView, self).post(request, *args, **kwargs)