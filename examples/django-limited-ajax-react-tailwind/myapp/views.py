from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def index(request):
    # TODO: Use a `render` template instead
    return HttpResponse(f"Hello {request.user.first_name}")
