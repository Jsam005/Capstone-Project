from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import login, logout
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, RegistrationForm, UserProfileForm
from .models import UserProfile

# Create your views here.


def login_view(request):
    # User login
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            #return redirect('account/profile/{}'.format(username))
            return redirect('account:profile')
    return render(request, 'account/login_form.html', {"form": form})

def logout_view(request):
    # Logs the User out and redirects to a page that gives you the option to log back in
    logout(request)
    return render(request, 'account/logout.html', {})

def register_view(request):
    # Registers new users
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        form.save()
        login(request, user)
        return redirect('account:profile')
    return render(request, 'account/registration_form.html', {"form": form})

def create_profile(request):
    form = UserProfileForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('account:profile')
    else:
        form = UserProfileForm()
        return render(request, 'account/update_profile.html', {'form': form})

# def profile_view(request, username):
#     user = get_object_or_404(User, username=username)
#     profile = get_object_or_404(UserProfile, user=user)
#     context = {
#         'user': user,
#         'profile': profile
#     }
#     return render(request, 'account/profile.html', context)

def profile_view(request):
    # Users profile
    user_profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'user_profile': user_profile
    }
    return render(request, 'account/profile.html', context)

@login_required
def update_profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(initial={
        'location': user_profile.location,
        'birthdate': user_profile.birthdate,
        'biography': user_profile.biography,
        'profile_image': user_profile.profile_image
    })
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = UserProfile.objects.get(user=request.user)

            location = form.cleaned_data['location']
            user_profile.location = location

            birthdate = form.cleaned_data['birthdate']
            user_profile.birthdate = birthdate

            biography = form.cleaned_data['biography']
            user_profile.biography = biography

            profile_image = form.cleaned_data['profile_image']
            user_profile.profile_image = profile_image
            user_profile.save()
            return redirect('account:profile')
    else:
        form = UserProfileForm()
    return render(request, 'account/update_profile.html', {'form': form})

def change_password_view(request):
    # Allows you to change your password while keeping you logged in
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('account:profile')
        else:
            return redirect('account:change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'account/change_password.html', {'form': form})

def delete():
    pass



