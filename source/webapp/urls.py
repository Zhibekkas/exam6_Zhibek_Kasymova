from django.urls import path
from webapp.views import (index, add, edit, guest_delete)


urlpatterns = [
    path('', index, name="index"),
    path('guest/add/', add, name="add"),
    path('guest/<int:pk>/edit', edit, name="edit"),
    path('guest/<int:pk>/delete', guest_delete, name="guest_delete")
]
