from django.urls import path
from events.views import show_events, add_event, show_events_detail, join_event

app_name = 'events'

urlpatterns = [
    path('events/', show_events, name='show_events'),
    path('events/add-event/', add_event, name='add_event'),
    path('events/<str:id>/', show_events_detail, name='show_events_detail'),
    path('events/<str:id>/join/', join_event, name='join_event'),
]