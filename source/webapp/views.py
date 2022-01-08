from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Guest, status_choices
from webapp.forms import GuestForm
from django.urls import reverse

# Create your views here.


def index(request):
    guests = Guest.objects.order_by("creation_date").filter(status='active')
    return render(request, 'index.html', {'guests': guests})


def edit(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'GET':
        form = GuestForm(initial={
            'name': guest.name,
            'email': guest.email,
            'text': guest.text,
            'status': guest.status
        })
        return render(request, 'edit.html', {"guest": guest, "form": form})
    else:
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest.name = request.POST.get('name')
            guest.email = request.POST.get('email')
            guest.text = request.POST.get('text')
            guest.status = request.POST.get('status')
            guest.save()
            return redirect("index", pk=guest.pk)
        return render(request, 'edit.html', {"guest": guest, "form": form})


