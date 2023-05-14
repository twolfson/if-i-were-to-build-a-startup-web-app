from django import template

register = template.Library()


@register.inclusion_tag("widgets/input.html")
def input(widget):
    # https://github.com/django/django/blob/4.2.1/django/forms/boundfield.py#L84-L106
    return {"widget": widget}
