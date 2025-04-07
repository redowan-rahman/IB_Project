from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import RegisterForm
from users.models import Profile
from users.models import ProfileForm

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Welcome {username} to Fitness Buddy')
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, 'register.html', {'form': form})

def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username, password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
    return render(request, 'login.html')

@login_required(login_url='login')
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('edit_profile')

    return render(request, 'profile.html', {'profile': profile})

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='dashboard')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)  # This ensures the profile is created if it doesn't exist

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = ProfileForm()

    return render(request, 'edit_profile.html', {'form': form})
