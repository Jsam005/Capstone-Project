from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import login, logout
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, RegistrationForm, EditProfileForm, CreateProfileForm
from .models import UserProfile

# Create your views here.

def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('account:profile')
        else:
            form = CreateProfileForm()
            return render(request, 'account/edit_profile.html', {'form': form})

def delete():
    pass

def login_view(request):
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

# def profile_view(request, username):
#     user = get_object_or_404(User, username=username)
#     profile = get_object_or_404(UserProfile, user=user)
#     context = {
#         'user': user,
#         'profile': profile
#     }
#     return render(request, 'account/profile.html', context)

# def register_view(request, username):
#     form = UserRegisterForm(request.POST or None)
#
#     if form.is_valid():
#         user = form.save()
#         password = form.cleaned_data.get('password')
#         user.set_password(user.password)
#         user.save()
#         new_user = authenticate(username=user.username, password=password)
#         login(request, new_user)
#         return redirect('account:profile/{}'.format(username))
#     return render(request, 'account/registration_form.html', {"form": form})

def register_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        form.save()
        login(request, user)
        return redirect('account:profile')
    return render(request, 'account/registration_form.html', {"form": form})

def profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'account/profile.html', context)

def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('account:edit-profile')
        else:
            form = EditProfileForm(instance=request.user)
            return render(request, 'account/edit_profile.html', {'form': form})

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


def logout_view(request):
    logout(request)
    return render(request, 'account/logout.html', {})
