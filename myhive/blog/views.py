from default.views import CategoryListMixin
from  django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Blog, Comment
from django import forms
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class BlogListView(ArchiveIndexView, CategoryListMixin):
    model = Blog
    date_field = 'posted'
    template_name = 'blog/blogs.html'
    paginate_by = 2
    allow_empty = True
    allow_future = True

    def get_queryset(self):
        blog = super(BlogListView, self).get_queryset()
        return blog


class BlogDetailView(DetailView, CategoryListMixin):
    model = Blog
    template_name = 'blog/blog.html'
    pk_url_kwarg = 'blog_id'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(blog_id=self.kwargs['blog_id'])
        form_comments = CommentForm
        context['form_comments'] = form_comments
        return context


class BlogCreateView(SuccessMessageMixin, CreateView, CategoryListMixin):
    model = Blog
    fields = ['title', 'description', 'content', 'is_commentable', 'user']
    success_url = reverse_lazy('blogs')
    success_message = 'Тему створено'


class BlogUpdateView(SuccessMessageMixin, UpdateView, CategoryListMixin):
    model = Blog
    fields = ['title', 'description', 'content', 'is_commentable', 'user']
    pk_url_kwarg = 'blog_id'
    success_url = reverse_lazy('blogs')
    success_message = 'Тему змінено'


class BlogDeleteView(DeleteView, CategoryListMixin):
    model = Blog
    pk_url_kwarg = 'blog_id'
    success_url = reverse_lazy('blogs')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse_lazy('blogs'))
        else:
            messages.add_message(request, messages.SUCCESS, 'Тему видалено')
            return super(BlogDeleteView, self).post(request, *args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {"content": 'Зміст'}


def comment_create(request, blog_id):

    if request.method == "POST" and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_id = Blog.objects.get(id=blog_id)
            comment.user = request.user.username
            form.save()
            request.session.set_expiry(60)
            request.session["pause"] = True

    return redirect('blog', blog_id)


