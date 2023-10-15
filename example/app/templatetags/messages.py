from django import template
from django.contrib import messages

register = template.Library()


@register.simple_tag
def message_level_to_card_class(level):
    if level == messages.INFO:
        return "bg-info"
    elif level == messages.SUCCESS:
        return "bg-success text-white"
    elif level == messages.WARNING:
        return "bg-danger text-white"
    elif level == messages.ERROR:
        return "bg-danger text-white"
    else:
        # DEBUG or anything else
        return ""
