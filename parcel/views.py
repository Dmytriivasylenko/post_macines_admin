from django.http import HttpResponse
from django.shortcuts import render
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
    return render(request, "one_parcel.html", context={'result': result})

def parcel_form_test(request, parcel_form=None):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form submitted successfully")
        else:
            return HttpResponse("Form error")
    first_parcel = models.Parcel.objects.get(pk=1)
    form = ParcelForm(first_parcel.as_dict())
    return render(request, "parcel_form.html", context={'form': form})