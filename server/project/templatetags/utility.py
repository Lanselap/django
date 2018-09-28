from django import template

register = template.Library()

@register.simple_tag
def get_value_by_rey(sourse, key):
    return sourse.get(key)
