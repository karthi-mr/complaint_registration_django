from django import template

register = template.Library()

def status(value: int):
    if value == 1: return "Not Solved"
    if value == 2: return "In Progress"
    if value == 3: return "Solved"
    if value == 4: return "Closed"


register.filter("process", status)