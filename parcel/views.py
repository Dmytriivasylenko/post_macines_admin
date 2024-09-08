from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

import parcel
from parcel import models
from parcel.form import ParcelForm
from parcel.models import Parcel


# Create your views here.
def parcel_view(request):
    user = request.user
    parcels = models.Parcel.objects.filter(recipient=user)
    return render(request, "parcels.html", context={'parcels': parcels})

def one_parcel_view(request, parcel_id):
    result = models.Parcel.objects.get(pk=parcel_id)
    if parcel.status is True:
        return render(request, "one_parcel.html", context={'result': result})

def parcel_form_test(request, parcel_form=None):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            first_parcel = models.Parcel.objects.get(pk=3)
            first_parcel.from_client(form.cleaned_data)
            first_parcel.save()
            return HttpResponse("Form submitted successfully")
        else:
            return HttpResponse("Form error")
    else:
        first_parcel = models.Parcel.objects.get(pk=1)
        form = ParcelForm(first_parcel.as_dict())
    return render(request, "one_parcel.html", context={'form': form})

def get_parcel(request):
    if request.method == 'POST':
        parcel = Parcel.objects.get(pk=request.POST['parcel_id'])
        parcel.status = True
        parcel.open_datetime = datetime.datetime.now()
        if parcel.order_datetime is None:
            parcel.open_datetime = datetime.datetime.now()

        parcel.save()

        parcel.locker.status = True
        parcel.locker.save()
        return redirect("/parcel")
