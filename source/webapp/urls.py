from django.urls import path
from webapp.views import (index, add, edit)


urlpatterns = [
    path('', index, name="index"),
    path('guest/add/', add, name="add"),
    path('guest/<int:pk>/edit', edit, name="edit")
]