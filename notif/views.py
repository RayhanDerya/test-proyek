from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from notif.models import Notif
from notif.forms import NotifForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@login_required(login_url='/login')
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
            return redirect('notif:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/login')
def show_notif(request):
    list_notif = Notif.objects.all()
    
    context ={
        'notif' : list_notif
    }

    return render(request, 'notif.html', context)

def create_notif(request):
    form = NotifForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        notifikasi = form.save(commit=False)
        notifikasi.sender = request.user
        notifikasi.save()
        return redirect('notif:show_main')
    
    context = {'form': form}
    return render(request, "create_notif.html", context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('notif:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('notif:login')