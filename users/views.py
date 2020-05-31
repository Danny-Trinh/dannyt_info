from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"@{username} has been created! you may login")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        u_form = ProfileUpdateForm(request.POST)
        p_form = UserUpdateForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save
            messages.success(request, f'your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserRegisterForm(instance=request.user)
        p_form = UserRegisterForm(instance=request.user.profile)
    context = {'u_form': u_form,
               'p_form': p_form
               }
    return render(request, 'users/profile.html', context)


