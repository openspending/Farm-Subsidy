import random
from django.conf import settings


def google_api_key(request):
    return {'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY}


def header_class(request):
    return {'header_class': 'header_' + str(random.randint(1, 10))}
