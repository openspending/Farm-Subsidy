import csv, os, time
from optparse import make_option
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from data.models import Payment, Recipient, Scheme


class Command(BaseCommand):
    
    help = 'Loads data for a year from the simplified payment.txt data format into DB (2013 or newer)'
    args = '<country year delimiter>'
    
    option_list = BaseCommand.option_list + (
        make_option(
            '--ignore-existing',
            action="store_true",
            dest="ignore_existing",
            default=False,
            help="Don't check for already existing payments"),
        make_option(
            '--simulate',
            action="store_true",
            dest="simulate",
            default=False,
            help="Don't write to DB, mainly to get an impression of the percentage of name matches"),
    )
    
    def format_payment_zid(self, country, zid):
        return country + 'Z' + str(zid).zfill(7)
    
    def get_payment_start_zid(self, country):
        '''
        Introduction of new ID scheme in the form (example): DEZ0000005345
        for easier ordering, determination of latest id
        Format: [COUNTRY_CODE]Z[ID Number + 0s leading to 7 ciphers]
        '''
        print "Determination of ZID for payment (new ID system for easier ordering)"
        if Payment.objects.filter(countrypayment=country).count() == 0:
            print "No payments for country in DB. ZID numbering will start with 1."
            return 1
        p = Payment.objects.filter(countrypayment=country).order_by('-globalpaymentid')[0]
        prefix_code = country + 'Z'
        if p.globalpaymentid[0:3] != prefix_code:
            print "No ZID for country in DB. ZID numbering will start with 1."
            return 1
        id = int(p.globalpaymentid[3:]) + 1
        print "Latest ZID: %s" % p.globalpaymentid
        print "ZID numbering will start with %s" % id
        return id
    
    def format_recipient_zid(self, country, zid):
        return country + 'Z' + str(zid).zfill(7)
    
    def get_recipient_start_zid(self, country):
        '''
        Introduction of new ID scheme in the form (example): DEZ0000005345
        for easier ordering, determination of latest id
        Format: [COUNTRY_CODE]Z[ID Number + 0s leading to 7 ciphers]
        '''
        print "Determination of ZID for recipient (new ID system for easier ordering)"
        if Recipient.objects.filter(countryrecipient=country).count() == 0:
            print "No recipients for country in DB. ZID numbering will start with 1."
            return 1
        r = Recipient.objects.filter(countryrecipient=country).order_by('-globalrecipientid')[0]
        prefix_code = country + 'Z'
        if r.globalrecipientid[0:3] != prefix_code:
            print "No ZID for country in DB. ZID numbering will start with 1."
            return 1
        id = int(r.globalrecipientid[3:]) + 1
        print "Latest ZID: %s" % r.globalrecipientid
        print "ZID numbering will start with %s" % id
        return id
    
    
    def handle(self, country, year, delimiter, *args, **options):
        path = os.path.join(settings.ROOT_PATH, 'data', 'csv', country, 'payment_%s.txt' % year)
        print "Opening file at %s..." % path
        
        if not os.path.isfile(path):
            raise CommandError("File does not exist or is not a valid file format")
        
        if not options.get('ignore_existing') and \
                Payment.objects.filter(year=year, countrypayment=country).count() > 0:
            raise CommandError("There are already payments in the database for the given year and country (see --ignore-existing option)")
        
        msg = "\nThis will write the csv data to the farmsubsidy DB (you can run a simulation with the --simulate option).\n" \
            "Do you want to continue (y/n)?"
        confirm = raw_input(msg)
        if confirm != 'y':
            return False
        
        with open(path, 'rb') as csvfile:
            datareader = csv.reader(csvfile, delimiter=delimiter)
            first = True
            matches = 0
            total = 0
            start = time.time()
            
            zid = self.get_payment_start_zid(country)
            rzid = self.get_recipient_start_zid(country)
            
            cNameIndex = {}
            for row in datareader:
                if first:
                    cnt = 0
                    for cName in row:
                        cNameIndex[cName] = cnt
                        cnt += 1
                else:
                    rs = Recipient.objects.filter(name=row[cNameIndex['rName']])
                    if len(rs) > 0:
                        matches += 1
                    if not options.get('simulate', False):
                        if len(rs) == 0:
                            r = Recipient()
                            zid_str = self.format_recipient_zid(country, rzid)
                            r.recipientid = zid_str
                            r.recipientidx = zid_str
                            r.globalrecipientid = zid_str
                            r.globalrecipientidx = zid_str
                            r.name = row[cNameIndex['rName']]
                            r.adress1 = row[cNameIndex['rAdress1']]
                            r.adress2 = row[cNameIndex['rAdress2']]
                            r.zipcode = row[cNameIndex['rZipcode']]
                            r.town = row[cNameIndex['rTown']]
                            r.countrypayment = country
                            r.countryrecipient = country
                            r.save()
                            print "New recipient %s saved." % r.name
                        else:
                            r = rs[0]
                        scheme = None
                        try:
                            scheme = Scheme.objects.get(pk=row[cNameIndex['globalSchemeID']])
                        except Scheme.DoesNotExist:
                            print "Scheme %s not found, payment ommited." % row[cNameIndex['globalSchemeID']]
                        if scheme:
                            p = Payment()
                            zid_str = self.format_payment_zid(country, zid)
                            p.paymentid = zid_str
                            p.globalpaymentid = zid_str
                            p.recipient = r
                            p.globalrecipientidx = r.globalrecipientidx
                            p.scheme = scheme
                            try:
                                amountEuro = float(row[cNameIndex['amountEuro']])
                            except ValueError:
                                amountEuro = 0
                            p.amounteuro = amountEuro
                            try:
                                amountNC = float(row[cNameIndex['amountNationalCurrency']])
                            except ValueError:
                                amountNC = 0
                            p.amountnationalcurrency = amountNC
                            p.year = year
                            p.countrypayment = country
                            p.save()
                            print "Payment with ID %s saved." %zid_str 
                            zid += 1
                            total += 1
                first = False
            end = time.time()
            
            elapsed = end - start
            new = total - matches
            print "Time elapsed: %s" % elapsed
            print "Matches: %s" % matches
            print "New: %s" % new 
            print "Total: %s" %total
            
            percent = round(matches / float(total) * 100, 2)
            print "%s percent of recipient names matched." % percent
        