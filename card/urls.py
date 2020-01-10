from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^category/(?P<category_slug>[-\w]+)/$', list_of_cards_by_category, name='list_by_category'),
    path('', category_list, name='category_list'),
    path('card/<str:slug>/', card_detail, name='card_detail'),
    path('cards/', card_list, name='card_list'),
    path('card/create', new_card, name='new_card'),
    path('card/<str:slug>/del', card_delete, name='card_delete'),
    path('cards/delete', card_delete_list, name='card_delete_list'),
    path('card/<str:slug>/edit', card_edit, name='card_edit'),
    ]