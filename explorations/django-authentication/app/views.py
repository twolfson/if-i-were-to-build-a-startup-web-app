from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views

from app.forms import LoginForm


@login_required
def index(request):
    return render(request, "index.html")


# Extend https://github.com/django/django/blob/4.2.1/django/contrib/auth/views.py#L67-L76
class LoginView(auth_views.LoginView):
    form_class = LoginForm


# Inspired by this guide: https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
# https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView
class SignUpFormView(CreateView):
    template_name = "registration/sign_up.html"
    # DEV: UserCreationForm is used by Django Admin, hence no provided views, https://github.com/django/django/blob/4.2.1/django/contrib/auth/admin.py#L74  # noqa:E501
    form_class = UserCreationForm

    def form_valid(self, form):
        # Don't call `super().form_valid()` as it tries to redirect
        #   https://github.com/django/django/blob/4.2.1/django/views/generic/edit.py#L133-L136
        #   https://github.com/django/django/blob/4.2.1/django/views/generic/edit.py#L63-L65
        form.save()

        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect("index")
