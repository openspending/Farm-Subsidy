import urllib

from django.template import Library

register = Library()


@register.simple_tag
def parse_qs(qs, k=None, v=None):
    qs = qs.copy()
    if k:
        qs[k] = v
    # Normally, we don't want to keep the page element of the string
    if 'page' in qs:
        del qs['page']
    return "?%s" % urllib.urlencode(
        dict([(key, val.encode('utf-8')) for key, val in qs.items()])
    )
