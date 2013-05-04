# encoding: utf-8
from django.db import models
from django.db.models import Sum
from django.conf import settings

DEFAULT_YEAR = settings.DEFAULT_YEAR


class SchemeManager(models.Manager):
    """
    Various reusable queries, like top_schemes
    """

    def get_query_set(self):
        return super(SchemeManager, self).get_query_set().filter(
                total__isnull=False)

    def top_schemes(self, country=None, year=DEFAULT_YEAR, limit=10):
        """
        Top schemes for a given country over all years.
        """
        kwargs = {}
        if country and country != "EU":
            kwargs['countrypayment'] = country

        schemes = self.get_query_set().filter(**kwargs)\
                .exclude(total=None).order_by('-total')
        return schemes[:limit]


class SchemeYearManager(models.Manager):
    """
    Various reusable queries, like top_schemes
    """

    def get_query_set(self):
        return super(SchemeYearManager, self).get_query_set().filter(
                total__isnull=False)

    def top_schemes(self, country=None, year=DEFAULT_YEAR):
        kwargs = {}
        if int(year) != 0:
            kwargs['year'] = year
        if country and country is not "EU":
            kwargs['countrypayment'] = country

        schemes = (self.get_query_set()
            .filter(**kwargs)
            .select_related('globalschemeid')
            .annotate(scheme_total=Sum('total'))
            .order_by('-scheme_total'))
        return schemes
