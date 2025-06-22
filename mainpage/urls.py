from django.urls import path
from . import views

urlpatterns = [

    path('articles/<int:article_id>/update/', views.update_article, name='update_article'),
]