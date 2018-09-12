from django.shortcuts import render
from django import forms
from .models import Guestbook
from django.shortcuts import redirect
from good.models import Category
from django.contrib import messages

# Create your views here.


class GuestbookForm(forms.ModelForm):
    class Meta:
        model = Guestbook
        fields = ['user', 'content']
        labels = {"user": 'Користувач', "content": 'Зміст'}



def good_create(request):
    books = Guestbook.objects.all()
    cats = Category.objects.order_by('name')

    if request.method == "POST":
        form = GuestbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook')
        #else:
            #return render(request, "good_add.html", {"category": cat, "form": form})
    else:
        form = GuestbookForm()
    return render(request, "guestbook/guestbook.html", {"form": form, "books": books, "cats": cats})
