from django.urls import path
from . import views

urlpatterns = [
    path('shortener/', views.create_short_url, name='create_short_url'),
    path('shortener/<short_code>', views.retrive_original_url_by_short_url, name='retrive_url'),
]
