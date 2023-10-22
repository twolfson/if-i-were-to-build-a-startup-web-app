from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.messages import get_messages


@require_http_methods(["GET"])
def messages(request):
    # https://github.com/jgerigmeyer/jquery-django-messages-ui/blob/2.0.2/messages_ui/middleware.py#L45-L55
    # https://docs.djangoproject.com/en/4.2/ref/contrib/messages/#displaying-messages
    message_list = [
        {
            "message": message.message,
            "level": message.level,
            "tags": message.tags,
        }
        for message in get_messages(request)
    ]

    return JsonResponse(message_list)
