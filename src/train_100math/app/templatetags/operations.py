from django import template

register = template.Library()


@register.filter(name='replace_op')
def replace_op(value):
    expr = value.split()
    op = expr[1]
    if op == '*':
        expr[1] = '×'
    elif op == '/%':
        expr[1] = '÷'
    return " ".join(expr)
