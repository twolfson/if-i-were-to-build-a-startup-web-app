from django import template

register = template.Library()


@register.inclusion_tag("widgets/input.html")
def input(widget):
    print('uhh', widget)
    print(widget.type, widget.value)
    return {"widget": widget}
