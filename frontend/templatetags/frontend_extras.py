import logging

from django import template
import os, json
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def my_split(my_str):
    if my_str is None:
        return []

    return [s.strip() for s in my_str.split(",")]


@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    concatenated = f"{arg1}{arg2}"
    return concatenated


@register.filter()
def minus_one(n):
    return n - 1


@register.filter()
def plus_one(n):
    return n + 1


@register.filter()
def my_range(n):
    return range(1, n + 1)


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='filename')
def filename(value):
    return os.path.basename(value.name)


@register.filter(name='my_float')
def my_float(value):
    try:
        return str(round(value, 2)).replace(",", ".")
    except Exception as e:
        return str(value).replace(",", ".")


@register.filter(name='lastname')
def lastname(value):
    """
    Returns the first character of lastname in lowercase for a given name
    """
    if value:
        return value[:2].upper()  # get the first letter of last name in lower case
    else:
        return "A"


@register.filter(name='name')
def name(created_by):
    """
    Returns the first character of lastname in lowercase for a given name
    """
    try:
        if created_by:
            return f"{created_by.first_name} {created_by.last_name.upper()}"
    except Exception as e:
        logging.exception(e)

    return "Talk To Web"


@register.filter(name='js', is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))


@register.filter()
def my_range(n):
    return range(1, n + 1)
