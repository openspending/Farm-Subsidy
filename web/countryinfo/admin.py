from django.contrib import admin
from models import CountryInfo, TransparencyScore


class CountryInfoAdmin(admin.ModelAdmin):
    list_display = ('country', 'original_source_name', 'download_filename',)

admin.site.register(CountryInfo, CountryInfoAdmin)
admin.site.register(TransparencyScore)
