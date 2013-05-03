import os
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--country', '-c', dest='country',),
        make_option('--table', '-t', dest='table',),
    )

    def __init__(self):
        super(Command, self).__init__()
        self.cursor = connection.cursor()

    def format_file_name(self, table, country):
        path = os.path.join(settings.ROOT_PATH, 'data', 'csv',
                     country, '%s.txt' % table)
        if path.startswith('/private'):
            # Hack for OS X :(
            path = "/" + "/".join(path.split('/')[2:])
        if os.path.exists(path):
            return path
        else:
            raise IOError('Data file not found at %s' % path)

    def delete_for_scheme(self, country):
        sql = '''BEGIN;
            DELETE FROM data_schemeyear WHERE countrypayment='%(country)s';
            DELETE FROM data_recipientschemeyear WHERE country='%(country)s';
            COMMIT;''' % {'country': country}
        print sql
        self.cursor.execute(sql)

    def delete_for_recipient(self, country):
        sql = '''BEGIN;
            DELETE FROM data_recipientyear WHERE country='%(country)s';
            COMMIT;''' % {'country': country}
        print sql
        self.cursor.execute(sql)

    def delete_country(self, table, country):
        if hasattr(self, 'delete_for_%s' % table):
            getattr(self, 'delete_for_%s' % table)(country)
        sql = """
            DELETE FROM data_%(table)s WHERE countrypayment = '%(country)s'; COMMIT;
        """ % {
            'country': country,
            'table': table,
        }
        print sql
        self.cursor.execute(sql)

    def copy(self, table, country):
        filename = self.format_file_name(table, country)
        columns = self.get_columns(table)
        sql = """
            COPY data_%(table)s (%(columns)s)
            FROM '%(filename)s'
            WITH CSV DELIMITER ';' QUOTE '\"' HEADER ENCODING 'Utf-8';;
            COMMIT;
        """ % {
            'filename': filename,
            'columns': columns,
            'table': table,
        }
        print sql
        self.cursor.execute(sql)

    def get_columns(self, table):
        columns = {
            'scheme': ['globalschemeid', 'namenationallanguage', 'nameenglish', 'budgetlines8digit', 'countrypayment'],
            'recipient': ['recipientid', 'recipientidx', 'globalrecipientid', 'globalrecipientidx', 'name', 'address1', 'address2', 'zipcode', 'town', 'countryrecipient', 'countrypayment', 'geo1', 'geo2', 'geo3', 'geo4', 'geo1nationallanguage', 'geo2nationallanguage', 'geo3nationallanguage', 'geo4nationallanguage', 'lat', 'lng'],
            'payment': ['paymentid', 'globalpaymentid', 'globalrecipientid', 'globalrecipientidx', 'globalschemeid', 'amounteuro', 'amountnationalcurrency', 'year', 'countrypayment'],
        }
        return ",".join(columns[table])

    def handle(self, **options):

        if not options.get('country'):
            raise Exception('Please specify a country.')
        else:
            country = options['country']

        if options.get('table', False):
            tables = [options['table']]
        else:
            tables = ['recipient', 'scheme', 'payment']

        for table in reversed(tables):
            self.delete_country(table, country)
        for table in tables:
            self.copy(table, country)
