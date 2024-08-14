from django.urls import path

import parcel.views

urlpatterns = [
    path('', parcel.views.parcel_view),
    path('<parcel_id>/', parcel.views.one_parcel_view)
]