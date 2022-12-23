from django.shortcuts import render
from .forms import UserCreateForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def signup(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse('Invalid form!')
    else:
        form = UserCreateForm()     
    return render(request, 'signin.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)  
        
        if user is not None:
            if user.is_active:
                login(request, user)
                logedin = True
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Not active!')
        else:
            return HttpResponse('Failed while authentication!')
        
    else: 
        return render(request, 'signout.html', {})