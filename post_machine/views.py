from django.http import HttpResponse
from post_machine import models


# Create your views here.

def locker_view(request, machine_id):
    one_postmachine = models.PostMachine.objects.get(PostMachine=machine_id)
    postmachine_lockes = models.Locker.objects.filter(post_machine=one_postmachine)
    return HttpResponse(f"ok, {one_postmachine} -> {[itm for itm in postmachine_lockes]}")

