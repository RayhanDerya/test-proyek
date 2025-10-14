from django.forms import ModelForm
from notif.models import Notif

class NotifForm(ModelForm):
    class Meta:
        model = Notif
        fields = ["receiver", "message"]