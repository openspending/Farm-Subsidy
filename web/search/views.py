# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response

from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery

from data.models import Recipient

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
        form = forms.SearchForm(initial={'q': q})

        auto_q = AutoQuery(q)
        sqs = SearchQuerySet().models(Recipient).facet('country').filter(content=auto_q)
        if request.GET.get('country', None) is not None:
            sqs = sqs.filter(country=request.GET['country'])

        total = 0
        offset = 0
        if request.GET.get('page'):
            offset = 20 * (int(request.GET.get('page')) - 1)
        for t in sqs[offset:offset + 20]:
            if t.total:
                total += t.total
        len(sqs)

    if search_map:
        t = 'map.html'
    else:
        t = 'results.html'
    return render_to_response(
        t,
        {
            'q': q,
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
