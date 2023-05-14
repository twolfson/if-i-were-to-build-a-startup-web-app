from allauth.account.decorators import verified_email_required
from django.shortcuts import render


# TODO: Page doesn't redirect to require verification, which seems strange?
@verified_email_required
def index(request):
    return render(request, "index.html")
