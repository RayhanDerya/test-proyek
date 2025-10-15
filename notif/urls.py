from django.urls import path
from notif.views import show_main, show_notif, create_notif, register, login_user,logout_user
from events.views import show_events, add_event
app_name = 'notif'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-notif/', create_notif, name='create_notif'),
    path('notif/', show_notif, name='show_notif'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('events/', show_events, name='show_events'),
    path('events/add-event/', add_event, name='add_event'),

]