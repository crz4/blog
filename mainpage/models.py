# товар/models.py
from django.db import models

class Товар(models.Model):
    название = models.CharField(max_length=100)
    описание = models.TextField()
    цена = models.DecimalField(max_digits=10, decimal_places=2)
    дата_добавления = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.название