from django.urls import path

import parcel.views

urlpatterns = [
    path('', parcel.views.parcel_view),
    path('get_parcel/', parcel.views.get_parcel),
    path('<parcel_form>/', parcel.views.parcel_form_test),
    path('<parcel_id>/', parcel.views.one_parcel_view)

]