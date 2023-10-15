from django import template

register = template.Library()


@register.inclusion_tag("widgets/input.html")
def input(widget):
    return {"widget": widget}


@register.inclusion_tag("widgets/checkbox.html")
def checkbox(widget):
    return {"widget": widget}
