from django.urls import path
from . import views

urlpatterns = [
    path('shortener/', views.create_short_url, name='create_short_url'),
    path('shortener/<str:short_code>', views.retrive_update_delete_url, name='retrive_or_update_url'),
    path('shortener/<str:short_code>/stats/', views.get_url_statistics, name='url_statistics'),
]
