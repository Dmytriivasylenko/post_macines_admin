from datetime import timezone, datetime

from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponse

from post_machine.models import PostMachine


class Parcel(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=200)
    size = models.IntegerField()
    post_machine_recipient = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    order_datetime = models.DateTimeField("date published")
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



