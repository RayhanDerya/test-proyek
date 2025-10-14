from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notif(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_notifs', null=True)
    receiver = models.CharField()
    message = models.TextField()
