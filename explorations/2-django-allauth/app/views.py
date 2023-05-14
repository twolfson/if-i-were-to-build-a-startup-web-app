from allauth.account.decorators import verified_email_required
from django.contrib import messages
from django.shortcuts import render


@verified_email_required
def index(request):
    return render(request, "index.html")


@verified_email_required
def message_test(request):
    messages.info(request, "Hello World!")
    return render(request, "index.html")
