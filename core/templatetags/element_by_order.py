from django import template

register = template.Library()

@register.filter
def by_order(queryset, order):
    return queryset.get(order = order)

