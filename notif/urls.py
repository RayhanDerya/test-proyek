from django.urls import path
from notif.views import show_main, show_notif, create_notif

app_name = 'notif'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-notif/', create_notif, name='create_notif'),
    path('notif/', show_notif, name='show_notif')
]