from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.views import LoginView, RedirectURLMixin, LogoutView
from django import forms
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url, render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import TemplateView, FormView


class UserLoginView(LoginView):
    next_page = '/'
    redirect_authenticated_user = False

class UserLogoutView(LogoutView):
    next_page = '/'


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields = ['username','password1','password2']



def sign_up(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'registration/registration.html', {'form': form})

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect("../login")
        else:
            return render(request, 'registration/registration.html', {'form': form})
    else:
        return
