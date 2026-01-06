from django import template

register = template.Library()

@register.filter
def split(value, key):
    return value.split(key)
{% load static %}
{% load custom_filters %}
