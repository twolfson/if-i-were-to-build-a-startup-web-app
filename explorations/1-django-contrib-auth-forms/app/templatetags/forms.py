from django import template

register = template.Library()


@register.inclusion_tag("widgets/input.html")
def input(widget):
    # https://github.com/django/django/blob/4.2.1/django/forms/boundfield.py#L325-L330
    print('wat', widget.type)
    return {"widget": {**widget.data, "wrap_label": True}}
