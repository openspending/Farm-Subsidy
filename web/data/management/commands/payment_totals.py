# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.models import Sum

from data.models import Recipient, Payment


class Command(BaseCommand):

    def handle(self, **options):

        total_recipients = Recipient.objects.count()
        sum_of_payments = int(Payment.objects.aggregate(total=Sum('amounteuro'))['total'])

        file_path = "%s/data/stats/payment_totals.txt" % settings.ROOT_PATH
        totals_file = open(file_path, 'w')
        totals_file.write("%s,%s" % (total_recipients, sum_of_payments))
        totals_file.close()
