from django.db import models

# Create your models here.
class Guestbook(models.Model):
    class Meta:
        ordering =['-posted']
        verbose_name = "запис гостьової книги"
        verbose_name_plural = "записи гостьової книги"

    user = models.CharField(max_length=20, verbose_name="Користувач")
    posted = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Публікація")
    content = models.TextField(verbose_name="Зміст")

    def __str__(self):
        return self.user + ' '+self.content[0:20]