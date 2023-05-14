from django import template

register = template.Library()


@register.inclusion_tag("widgets/input.html")
def input(bound_field):
    # https://github.com/django/django/blob/4.2.1/django/forms/boundfield.py#L84-L106
    self = bound_field
    widget = None
    attrs = None
    only_initial = False

    widget = widget or self.field.widget
    if self.field.localize:
        widget.is_localized = True
    attrs = attrs or {}
    attrs = self.build_widget_attrs(attrs, widget)
    if self.auto_id and "id" not in widget.attrs:
        attrs.setdefault(
            "id", self.html_initial_id if only_initial else self.auto_id
        )
    if only_initial and self.html_initial_name in self.form.data:
        # Propagate the hidden initial value.
        value = self.form._widget_data_value(
            self.field.hidden_widget(),
            self.html_initial_name,
        )
    else:
        value = self.value()
    print(self.form.renderer)
    return {"widget": dict(name=self.html_initial_name if only_initial else self.html_name, value=value, attrs=attrs)}
