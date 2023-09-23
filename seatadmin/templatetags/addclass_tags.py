from django import template

register = template.Library()


@register.filter(name='addclass')
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})

