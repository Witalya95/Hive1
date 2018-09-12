from django.urls import path
from .views import ProfileTemplateView, ProfileUpdateView

urlpatterns = [

    #Профіль користувача

    path('profile/', ProfileTemplateView.as_view(template_name='users/profile.html'), name='profile'),
    path('edit/<int:user_id>', ProfileUpdateView.as_view(template_name='users/user_form.html'), name='profile_edit'),

]