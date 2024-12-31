from django import template

register = template.Library()

@register.simple_tag
def active_class(current_path, expected_path):
    return "active" if current_path == expected_path else current_path