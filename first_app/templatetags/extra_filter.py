from django import template
register=template.Library()

@register.filter(name='addy')
def addy(value):
    if len(value)<=1:
        return (str(value)+'y')
    else:
        word=[]
        value=value.split( )
        for x in value:
            word.append(x+'y')
        return (' ').join(word)
