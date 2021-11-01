from django import template

register = template.Library()

def my_cut(value, arg):
    return value.replace(arg, "")

register.filter("my_cut", my_cut)