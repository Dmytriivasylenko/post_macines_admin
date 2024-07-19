from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def parcel_view(request):
    return HttpResponse("Hello, world. You're at the polls list. parcels view")

def one_parcel_view(request, parcel_id):
    return HttpResponse("Hello, world. You're at the polls list. one parcel views")