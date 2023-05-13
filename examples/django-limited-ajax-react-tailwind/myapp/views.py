from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

@login_required
def index(request):
    return render(request, "index.html")

class SignUpFormView(CreateView):
    template_name = "registration/sign_up.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        # Don't call `super().form_valid()` as it tries to redirect
        #   https://github.com/django/django/blob/4.2.1/django/views/generic/edit.py#L133-L136
        #   https://github.com/django/django/blob/4.2.1/django/views/generic/edit.py#L63-L65
        form.save()

        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        # DEV: Don't call form_valid() as it'll want to use a success URL, https://github.com/django/django/blob/4.2.1/django/views/generic/edit.py#L63-L65
        return redirect('index')
