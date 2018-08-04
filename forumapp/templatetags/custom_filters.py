from random import randint
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def rand_color(s):
    """
    Generates random color
    """
    color = "%06x" % randint(0, 0xFFFFFF)
    return s.replace(' ', color)


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def sort_by(queryset, order):
    return queryset.order_by(order)