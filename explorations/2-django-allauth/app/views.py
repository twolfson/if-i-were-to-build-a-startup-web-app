from allauth.account.decorators import verified_email_required
from django.shortcuts import render


@verified_email_required
def index(request):
    return render(request, "index.html")
