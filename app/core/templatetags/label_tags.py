import datetime
from django import template
from lrr.labels import get_label as get_label_util

register = template.Library()


@register.simple_tag
def get_label(name) -> str:
    return get_label_util(name)
