from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    SPORT_CHOICES = [
        ('futsal','Futsal'),
        ('basket','Basket')
    ]

    sport = models.CharField(max_length=20, choices=SPORT_CHOICES, default='Futsal')
    startdate = models.DateField()
    participant = models.IntegerField(default=0)

    def increment_participant(self):
        self.participant +=1
        self.save()

class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='joined_events')
    events = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_participant')