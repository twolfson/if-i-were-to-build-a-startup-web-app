from django import template

register = template.Library()


@register.inclusion_tag("widgets/input.html")
def input(widget, **attrs):
    return {"widget": widget, "attrs": attrs}
