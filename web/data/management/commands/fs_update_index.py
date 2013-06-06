from django.core.management.base import BaseCommand
from django.db.models import get_model
from django.db import reset_queries, connection

from haystack import connections as haystack_connections
from haystack.exceptions import NotHandled


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.cursor = connection.cursor()

    def update_index(self, labels, batch_size=5000):
        for label in labels:
            model = get_model(*label)
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
                for qs in self.get_query_sets(all_qs, batch_size=batch_size):
                    backend.update(index, qs)

    def get_query_sets(self, qs, batch_size):
        """
        Instead of getting chunks by offset which is
        inefficient, we get them by ordering and pk > last_pk
        and limiting.
        """
        total = qs.count()
        last_pk = None
        for start in range(0, total, batch_size):
            small_qs = qs.all()
            if last_pk is not None:
                small_qs = small_qs.filter(pk__gt=last_pk)
            small_qs = small_qs[:batch_size]
            objs = list(small_qs)
            yield objs
            last_pk = objs[-1].pk
            print "  indexed %s - %d of %d." % (
                    last_pk, start + batch_size, total)
            reset_queries()

    def handle(self, **options):
        self.update_index([s.split('.') for s in
            ('data.Recipient',
            'data.Location',
            'features.Feature')
        ])
