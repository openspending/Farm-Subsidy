from django.db import models


class TransparencyScore(models.Model):
    country = models.CharField(blank=False, max_length=2, primary_key=True)
    score = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.country


class CountryInfo(models.Model):
    country = models.CharField(blank=False, max_length=2, primary_key=True)
    original_source_name = models.CharField(max_length=85, blank=True)
    original_source_url = models.URLField(blank=True)
    original_source_instructions = models.TextField(blank=True)
    download_filename = models.CharField(max_length=85, blank=True)
    download_size = models.CharField(max_length=10, blank=True)

def __unicode__(self):
        return self.country

