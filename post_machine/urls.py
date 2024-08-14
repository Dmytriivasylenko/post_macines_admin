from django.urls import path
import post_machine.views

urlpatterns = [
    path('<machine_id>/', post_machine.views.locker_view),
]