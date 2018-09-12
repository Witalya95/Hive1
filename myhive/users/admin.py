from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import User

from .models import UProfile

# Register your models here.


class UProfileInlite(admin.StackedInline):
    model = UProfile


class UserAdmin(auth_admin.UserAdmin):
    inlines = (UProfileInlite,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
