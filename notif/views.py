from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from notif.models import Notif
from notif.forms import NotifForm

# Create your views here.
def show_main(request):
    context = {
        'test' : 'INI TEST PROYEK.'
    }

    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def show_notif(request):
    list_notif = Notif.objects.all()
    
    context ={
        'notif' : list_notif
    }

    return render(request, 'notif.html', context)

def create_notif(request):
    form = NotifForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('notif:show_main')
    
    context = {'form': form}
    return render(request, "create_notif.html", context)
    
