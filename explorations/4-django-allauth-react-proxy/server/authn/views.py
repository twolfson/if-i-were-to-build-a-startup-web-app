from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def messages(request):
    # https://github.com/jgerigmeyer/jquery-django-messages-ui/blob/2.0.2/messages_ui/middleware.py#L45-L55
    message_list = [
        {
            "level": message.level,
            "message": text_type(message.message),
            "tags": message.tags,
        }
        for message in messages.get_messages(request)
    ]

    return JsonResponse(message_list)
