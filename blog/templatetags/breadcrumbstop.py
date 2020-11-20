from django import template


register = template.Library()


@register.filter(name = 'breadcrumbs', is_safe = False)
def breadcrumbs(val):
    try:
        int_val = int(val)
    except:
        pass

    if int_val==0:
        return 'EPL'
    elif int_val==1:
        return 'Laliga'
    
    else:
        pass