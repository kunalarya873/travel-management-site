from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """ Add a CSS class to a form field. """
    if hasattr(field, 'widget'):
        # Update the widget attributes
        current_classes = field.field.widget.attrs.get('class', '')
        new_classes = f'{current_classes} {css_class}'.strip()
        field.field.widget.attrs['class'] = new_classes
    return field
