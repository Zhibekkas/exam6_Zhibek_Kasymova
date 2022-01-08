from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Guest, status_choices

# Create your views here.


def index(request):
    guests = Guest.objects.order_by("creation_date")
    return render(request, 'index.html', {'guests': guests})


