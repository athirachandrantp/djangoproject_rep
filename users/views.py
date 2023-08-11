from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .forms import customUserCreationForm, ProfileForm, SkillForm

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
            return redirect('edit-account')
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

@login_required(login_url='login')
def user_account(request):
    profile = request.user.profile

    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)
@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def createskill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'skill was added successfully')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)

@login_required(login_url='login')
def updateskill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'skill was updated')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)

def deleteskill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'skill was deleted')
        return redirect('account')
    context = {'object': skill}
    return render(request, 'delete_object.html', context)

