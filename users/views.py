from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
# Create your views here.


class UserLoginView(auth_views.LoginView):
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        return context


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

    context = {'form': form,
               'title': "Join Today"
               }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        # u_form = UserUpdateForm(request.POST)
        p_form = ProfileUpdateForm(request.POST)
        # if u_form.is_valid() and p_form.is_valid():
        if p_form.is_valid():
            # u_form.save()
            p_form.save()
            messages.success(request, f'your account has been updated!')
            return redirect('profile')
    else:
        # u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
               'p_form': p_form,
               'title': "Your Profile"
               }
    return render(request, 'users/profile.html', context)


