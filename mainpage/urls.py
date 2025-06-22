from django.urls import path
from . import views

urlpatterns = [
    path('generate_table/', views.generate_table, name='generate_table'),
]