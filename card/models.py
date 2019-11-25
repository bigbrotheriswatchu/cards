from django.db import models

class Cards(models.Model):

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"

    title = models.CharField(max_length=30, db_index=True)
    text = models.TextField(max_length=100, db_index=True)

    def __str__(self):
        return self.text


class Translate(models.Model):
    title = models.CharField(blank=True, max_length=30, db_index=True)
    card = models.OneToOneField(Cards, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
