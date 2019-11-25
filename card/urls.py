from django.urls import path
from .views import *


urlpatterns = [
    path('', card_list, name='card_list_url'),
    path('card/<int:pk>/', card_detail, name='card_detail'),
    ]