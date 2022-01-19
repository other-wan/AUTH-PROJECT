
from django.shortcuts import (render, redirect)
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash
)
from .forms import (
    UserLoginForm,
    UserRegistrationForm,
    UserPasswordChangeForm
)


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful")
                return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', context={
        'form': form
    })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(reverse('accounts:login'))
    return render(request, 'logout.html', context=None)


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, f"User: {user.email} has been successfully created")
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', context={
        'form': form
    })


@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed successful")
            return redirect('/')
    else:
        form = UserPasswordChangeForm(user=request.user)
    return render(request, 'password_change.html', context={
        'form': form
    })
