from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .forms import customUserCreationForm

# Create your views here.
def loginpage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('users')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users')
        else:
            messages.error(request, 'username or password is incorrect')
    return render(request, 'users/login_register.html')

def logoutuser(request):
    logout(request)
    messages.info(request, 'user was logged-out')
    return redirect('login')

def registeruser(request):
    page = 'register'
    form = customUserCreationForm()

    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'user account was created!')

            login(request, user)
            return redirect('users')
        else:
            messages.success(
                request, 'an error has occurred during registration'
            )

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userprofile(request, pk):
    profile = Profile.objects.get(id=pk)

    topskills = profile.skill_set.exclude(description__exact="")
    otherskills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topskills': topskills, 'otherskills': otherskills}
    return render(request, 'users/user-profile.html', context)