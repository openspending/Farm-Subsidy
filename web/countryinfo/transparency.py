from django.contrib.humanize.templatetags.humanize import ordinal
from models import TransparencyScore


def transparency_score(country):
    try:
        ts = TransparencyScore.objects.get(country=country)
    except TransparencyScore.DoesNotExist:
        return None
    return {
        'rank': "%s" % (ordinal(ts.rank),),
        'percent': ts.score
    }


def transparency_list():
    pass
