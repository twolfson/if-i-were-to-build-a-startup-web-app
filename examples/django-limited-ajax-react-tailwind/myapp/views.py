from django.shortcuts import redirect
from django.http import HttpResponse

def index(request):
    # TODO: Redirect abstraction prob is widely applied as a mixin, no?
    if not request.user.is_authenticated:
        return redirect("/login")

    # TODO: Use a `render` template instead
    return HttpResponse(f"Hello {request.user.first_name}")
