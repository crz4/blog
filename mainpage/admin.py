# товар/admin.py
from django.contrib import admin
from .models import Товар

@admin.register(Товар)
class ТоварAdmin(admin.ModelAdmin):
    list_display = ['название', 'цена', 'дата_добавления']