from django.shortcuts import render, redirect, get_object_or_404
from events.forms import EventForm
from events.models import Event, UserEvent

# Create your views here.
def show_events(request):
    events = Event.objects.all()
    context = {
        'events' : events
    }

    return render(request, 'events.html', context)

def add_event(request):
    forms = EventForm(request.POST or None)
    if forms.is_valid() and request.method == 'POST':
        forms.save()
        return redirect('notif:show_main')
    
    context = {'forms': forms}
    return render(request, "create_events.html", context)

def show_events_detail(request, id):
    event = get_object_or_404(Event, pk=id)

    context = {
        'event': event
    }
    return render(request, 'event_details.html', context)

def join_event(request, id):
    event = get_object_or_404(Event, pk=id)
    user_event = UserEvent.objects.get_or_create(user=request.user, events=event)
    user_event.save()
    return redirect('notif:show_main')