from optparse import make_option

from django.core.management.base import BaseCommand
from django.db.models import get_model
from django.db import reset_queries

from haystack import connections as haystack_connections
from haystack.exceptions import NotHandled


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--country', '-c', dest='country',
            help='ISO country name'),
        make_option('--barch_size', '-b', dest='batch_size',
            type='int', default=1000, help='Batch Size'),
        make_option('--offset', '-o', dest='offset',
            default='', help='Offset Index to start from')
    )
    help = 'Load data into search index'

    def update_indexes(self, labels, **kwargs):
        for label in labels:
            model = get_model(*label)
            self.update_index(model, **kwargs)

    def update_index(self, model, batch_size=1000, country=None,
                     offset='', **kwargs):
        for using in haystack_connections.connections_info.keys():
            backend = haystack_connections[using].get_backend()
            unified_index = haystack_connections[using].get_unified_index()
            try:
                index = unified_index.get_index(model)
            except NotHandled:
                if self.verbosity >= 2:
                    print "Skipping '%s' - no index." % model
                continue
            print "Indexing %s" % model
            all_qs = model.objects.order_by(model._meta.pk.name)
            if country is not None:
                all_qs = all_qs.filter(countrypayment=country)
            for qs in self.get_query_sets(all_qs, batch_size=batch_size, last_pk=offset):
                backend.update(index, qs)

    def get_query_sets(self, qs, batch_size, last_pk=None):
        """
        Instead of getting chunks by offset which is
        inefficient, we get them by ordering and pk > last_pk
        and limiting.
        """
        if last_pk:
            total = qs.filter(pk__gt=last_pk).count()
        else:
            total = qs.count()
        for start in range(0, total, batch_size):
            small_qs = qs.all()
            if last_pk:
                small_qs = small_qs.filter(pk__gt=last_pk)
            small_qs = small_qs[:batch_size]
            objs = list(small_qs)
            yield objs
            last_pk = objs[-1].pk
            print "  indexed %s - %d of %d." % (
                    last_pk, start + batch_size, total)
            reset_queries()

    def handle(self, **options):
        self.update_indexes([s.split('.') for s in
            ('data.Recipient',)
        ], **options)
