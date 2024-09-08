import logging
from datetime import timezone, datetime
from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponse
from post_machine.models import PostMachine, Locker
from django.db.models.signals import post_save
from django.dispatch import receiver


class Parcel(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=200)
    size = models.IntegerField()
    post_machine_recipient = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    locker = models.ForeignKey(Locker, null=True, blank=True, default=None, on_delete=models.DO_NOTHING)
    order_datetime = models.DateTimeField("date published")
    open_datetime = models.DateTimeField("date published", null=True, blank=True)
    update_datetime = models.DateTimeField("date published", default=datetime.now)
    status = models.BooleanField("default=False")


    def as_dict(self):
        return {
            'recipient': self.recipient,
            'sender': self.sender,
            'size': self.size,
            'post_machine_recipient': self.post_machine_recipient,
            'order_datetime': self.order_datetime,
            'update_datetime': self.update_datetime,
            'status': self.status
        }

    def from_client(self, data):
        self.sender = data['sender']
        self.post_machine_recipient = data['post_machine_recipient']
        self.order_datetime = data['order_datetime']
        self.update_datetime = data['update_datetime']
        self.status = data['status']
        self.size = data['size']
        self.recipient = data['recipient']


@receiver(post_save, sender=Parcel)  # Connect to the built-in post_save signal
def update_status_on_parcel_put_to_locker(sender, instance, created, **kwargs):
    print(instance)
    if instance.status == False:
        if instance.locker is not None:
            parcel_locker = Locker.objects.get(pk=instance.locker.pk)
            parcel_locker.status = False
            parcel_locker.save()
            logging.info(f"updated status for parcel {instance}")

