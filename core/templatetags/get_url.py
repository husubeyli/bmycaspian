from django import template
from urllib.parse import urlparse

register = template.Library()


@register.filter
def get_url(full_path):
    full_url = urlparse(full_path)
    return full_url.path

