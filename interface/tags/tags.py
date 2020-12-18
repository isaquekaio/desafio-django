from django import template

register = template.Library()

@register.filter(name='getattribute')
def getattribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""
    if hasattr(value, arg):
        return getattr(value, arg)
    try:
        return value[arg]
    except (KeyError, TypeError):
        return ''
