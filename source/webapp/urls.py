from django.urls import path
from webapp.views import (index,
                          edit)


urlpatterns = [
    path('', index, name="index"),
    path('guest/<int:pk>/edit', edit, name="edit")
]