from django import template
from ..models import *
import math

register = template.Library()

@register.simple_tag
def call_sellPrice(price,discount):
    if discount is None and discount is 0:
        return price
    sellPrice = price
    sellPrice = price - (price * discount / 100)
    return math.floor(sellPrice)

@register.simple_tag
def progress_bar(total_quantity,availability):
    progress_bar = availability
    progress_bar = availability * (100/total_quantity)
    return math.floor(progress_bar)
    