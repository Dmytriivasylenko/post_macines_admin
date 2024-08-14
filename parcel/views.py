from django.http import HttpResponse
from django.shortcuts import render
from parcel import models
from parcel.models import Parcel


# Create your views here.
def parcel_view(request):
    user = request.user
    parcels = models.Parcel.objects.filter(recipient=user)
    return render(request, "parcels.html", context={'parcels': parcels})

def one_parcel_view(request, parcel_id):
    result = models.Parcel.objects.get(pk=parcel_id)
    return render(request, "one_parcel.html", context={'result': result})