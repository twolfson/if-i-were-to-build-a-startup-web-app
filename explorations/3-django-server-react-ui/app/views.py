# TODO: Demonstrate requirement via some other page
# from allauth.account.decorators import verified_email_required
from django.contrib import messages
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def message_test(request):
    messages.info(request, "Hello World!")
    messages.success(request, "Hello Again!")
    return render(request, "index.html")
