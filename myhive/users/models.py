from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Користувач'

    mobile_phone = models.CharField(max_length=12, blank=True, verbose_name='Номер мобільного', default='')
    city = models.CharField(max_length=30, blank=True, verbose_name='Місто', default='')

    def __str__(self):
        return self.user.username
