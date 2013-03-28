# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery

from data.models import Location, Recipient
from features.models import Feature
from listmaker.models import List

import forms


def search(request, search_map=False):
    form = forms.SearchForm()
    q = request.GET.get('q', '')
    total = 0
    offset = 0
    sqs = None
    list_search = None
    location_search = None
    feature_search = None

    if q:
        forms.SearchForm(initial={'q': q})

        auto_q = AutoQuery(q)
        sqs = SearchQuerySet().models(Recipient).filter(content=auto_q).load_all()

        total = 0
        offset = 0
        if request.GET.get('page'):
            offset = 20 * (int(request.GET.get('page')) - 1)
        for t in sqs[offset:offset + 20]:
            if t.object.total:
                total += t.object.total
        len(sqs)

        # Lists search:
        list_search = SearchQuerySet().models(
            List).filter(content=auto_q).load_all().highlight()

        # Location search:
        location_search = SearchQuerySet().models(Location).filter(content=auto_q)[:5]

        # Features search:
        feature_search = SearchQuerySet().models(Feature).filter(
            content=auto_q).filter(published=True).load_all().highlight()[:3]

    if search_map:
        t = 'map.html'
    else:
        t = 'results.html'
    return render_to_response(
        t,
        {
            'total': total,
            'offset': offset,
            'form': form,
            'sqs': sqs,
            'list_search': list_search,
            'location_search': location_search,
            'feature_search': feature_search
        },
        context_instance=RequestContext(request)
    )
