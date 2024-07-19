from django.urls import path

import parcel

urlpatterns = [
    path('', parcel.views.parcel_view),
    path('<machine_id>', parcel.views.one_parcel_view)


]