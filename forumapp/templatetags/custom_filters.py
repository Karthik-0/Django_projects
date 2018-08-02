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