# -*- coding: utf-8 -*-
import random
import socket
import urllib2

from django.core.urlresolvers import reverse
from django.conf import settings

from data import countryCodes


def country(request):
    countryCode = request.META['PATH_INFO'].split('/')[1].upper()

    try:
        country = countryCodes.country_codes(countryCode)
    except ValueError:
        country = {'code': ''}

    return {'country': country}


def ip_country(request):

    if not request.session.get('ip_country', None):
        try:
            timeout = 3
            socket.setdefaulttimeout(timeout)

            ip = request.META.get('REMOTE_ADDR')
            req = urllib2.Request('http://gaze.mysociety.org/gaze-rest?f=get_country_from_ip&ip=%s' % ip)
            ip_country = urllib2.urlopen(req).read()

            if len(ip_country) == 1:
                raise ValueError

            if ip_country not in countryCodes.country_codes():
                raise ValueError

            request.session['ip_country'] = ip_country

        except Exception:
            ip_country = countryCodes.country_codes()[random.randint(0, 22)]
            request.session['ip_country'] = ip_country
    else:
        ip_country = request.session.get('ip_country', None)

    return {'ip_country': {
                'ip_country': ip_country,
                'ip_country_name': countryCodes.country_codes(ip_country)['name']
    }}


def breadcrumb(request):
    breadcrumb = []
    path = request.META['PATH_INFO'].split('/')

    # First make the country breadcrumb:
    if path[1] in countryCodes.country_codes():
        country = countryCodes.country_codes(path[1])
        breadcrumb.append({
            'country': [
                {'name': country['name'],
                 'url': reverse('country', args=[country['code']])},
            ]})

    # Locations
    if 'location' in path and path[2] == "location" and len(path) >= 6:
        year = path[3]
        geos = ['geo1', 'geo2', 'geo3', 'geo4']
        locations = path[4:]
        location_breadcrumbs = []
        while locations:
            kwargs = {'country': country['code'], 'year': year}
            for i, geo in enumerate(geos):
                kwargs['slug'] = "/".join(locations)

            item = {
                'name': locations[-1],
                'url': reverse('location_view', kwargs=kwargs)
            }
            location_breadcrumbs.append(item)
            locations.pop()
        location_breadcrumbs[0]['class'] = 'selected'
        location_breadcrumbs.reverse()
        breadcrumb.append({'Sub-Locations': location_breadcrumbs})

    # Schemes
    if 'scheme' in path and 'admin' not in path and len(path) >= 5:
        scheme_breadcrumbs = []
        item = {
            'name': 'All Schemes',
            'url': reverse('all_schemes', kwargs={'country': country['code'], })
        }
        scheme_breadcrumbs.append(item)
        breadcrumb.append({'Schemes': scheme_breadcrumbs})

    return {'breadcrumbs': breadcrumb}


def data_totals_info(request):
    file_path = "%s/data/stats/payment_totals.txt" % settings.ROOT_PATH
    totals_file = open(file_path, 'r').read()
    (total_recipients, sum_of_payments) = totals_file.split(',')

    return {
        'total_recipients': total_recipients,
        'sum_of_payments': sum_of_payments,
    }
