from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from treebeard.mp_tree import MP_Node
from django.contrib.gis.db import models as geo_models

from managers.recipients import RecipientManager
from managers.schemes import SchemeManager

class Recipient(models.Model):
    recipientid = models.CharField(max_length=10)
    recipientidx = models.CharField(max_length=10)
    globalrecipientid = models.CharField(max_length=10)
    globalrecipientidx = models.CharField(max_length=10,primary_key=True)
    name = models.TextField(null=True)
    address1 = models.TextField(null=True)
    address2 = models.TextField(null=True)
    zipcode = models.CharField(max_length=20, null=True)
    town = models.TextField(null=True)
    countryrecipient = models.CharField(max_length=2, null=True, db_index=True)
    countrypayment = models.CharField(max_length=2, null=True, db_index=True)
    geo1 = models.TextField(null=True)
    geo2 = models.TextField(null=True)
    geo3 = models.TextField(null=True)
    geo4 = models.TextField(null=True)
    geo1nationallanguage = models.TextField(null=True)
    geo2nationallanguage = models.TextField(null=True)
    geo3nationallanguage = models.TextField(null=True)
    geo4nationallanguage = models.TextField(null=True)
    lat = models.FloatField(null=True, default=None)
    lng = models.FloatField(null=True, default=None)
    total = models.FloatField(null=True, db_index=True)

    objects = RecipientManager()

    def __unicode__(self):
        return "%s (%s)" % (self.pk, self.name)
    
    # class Meta():
    #     managed = False
    
    def get_absolute_url(self):
        return reverse('recipient_view', args=[self.countrypayment, self.pk, slugify(self.name)])
    
    def geo_url(self, geo_type):
        """
        Returns a URL (from reverse()) for a location.
        """

        geos = [self.geo1,self.geo2,self.geo3,self.geo4,]
        slug = "/".join([slugify(n) for n in geos[:geo_type]])
        return reverse('location_view', args=[self.countrypayment, slug])
    
    def geo1_url(self):
        return self.geo_url(1)

    def geo2_url(self):
        return self.geo_url(2)

    def geo3_url(self):
        return self.geo_url(3)

    def geo4_url(self):
        return self.geo_url(4)
        

class GeoRecipient(geo_models.Model):
    recipient = models.ForeignKey(Recipient, primary_key=True)
    location = geo_models.PointField()

    objects = geo_models.GeoManager()

    def __unicode__(self):
        return self.pk

class Payment(models.Model):
    paymentid = models.TextField()
    globalpaymentid = models.CharField(max_length=10, primary_key=True)
    globalrecipientid = models.TextField()
    recipient = models.ForeignKey(
                                Recipient, 
                                db_column='globalrecipientidx', 
                                max_length=10,
                                db_index=True,
                                )
    scheme = models.ForeignKey('Scheme', db_column='globalschemeid')
    amounteuro = models.FloatField(null=True, db_index=True) # This field type is a guess.
    amountnationalcurrency = models.FloatField(null=True) # This field type is a guess.
    year = models.IntegerField(db_index=True)
    countrypayment = models.CharField(max_length=4, default=None, db_index=True)

    # class Meta():
    #     managed = False


class Scheme(models.Model):
    globalschemeid = models.CharField(max_length=40, primary_key=True)
    namenationallanguage = models.TextField(null=True)
    nameenglish = models.TextField(db_index=True)
    budgetlines8digit = models.CharField(max_length=10, null=True)
    countrypayment = models.CharField(max_length=2)
    total = models.FloatField()
    
    objects = SchemeManager()
    
    def get_absolute_url(self):
        return reverse('scheme_view', args=[self.countrypayment, 
                                            self.pk, 
                                            slugify(self.nameenglish)])

class SchemeYear(models.Model):
    globalschemeid = models.CharField(blank=True, max_length=40, db_index=True)
    nameenglish = models.TextField(blank=True)
    countrypayment = models.CharField(blank=True, max_length=2)
    year = models.IntegerField(blank=True, null=True)
    total = models.FloatField()

class TotalYear(models.Model):
    recipient = models.ForeignKey(Recipient, db_index=True)
    year = models.IntegerField(blank=True, null=True, db_index=True)
    total = models.FloatField(db_index=True)
    country = models.CharField(blank=False, max_length=2)



class Location(MP_Node):

    geo_type = models.CharField(blank=True, max_length=10)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    country = models.CharField(blank=True, max_length=100)
    recipients = models.IntegerField(blank=True, null=True)
    total = models.FloatField()
    average = models.FloatField()
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('location_view', args=[self.country, self.slug])
    
