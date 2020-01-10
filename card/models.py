from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.urls import reverse


class Category(models.Model):

    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='card_image', blank=True)
    cards_count = models.PositiveIntegerField(default=0, verbose_name="Кол-во карточек")

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('card:list_by_category', args=[self.slug])

    def __str__(self):
        return self.title


class Cards(models.Model):

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"

    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="Категория")
    slug = models.SlugField(max_length=250, unique=True, )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    text = models.TextField(max_length=100, verbose_name="Слово")
    translate = models.CharField(max_length=100, verbose_name="Перевод")
    card_count = models.PositiveIntegerField(default=0, verbose_name="Кол-во карточек")

    def get_absolute_url(self):
        return reverse('card:card_list', args=[self.slug])

    def __str__(self):
        return self.text


