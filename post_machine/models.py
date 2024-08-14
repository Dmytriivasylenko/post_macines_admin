from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PostMachine(models.Model):
    adress = models.CharField(max_length=200)
    city = models.CharField(max_length=200)


class Locker(models.Model):
    size = models.IntegerField()
    post_machine_recipient_id = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


