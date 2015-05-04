import os, sys
from django.core.management.base import BaseCommand
from data.models import CountryYear


class Command(BaseCommand):

    help = 'Generate shell export commands for exporting data to a flat, denormalized CSV file format (Postgres specific)'
    args = '<country_list(comma separated, min. one country) python_path(path to python interpreter) managepy_path(path to manage.py file) path(path to store exported data) year_list(comma separated, optional, default: all years)>'

    def handle(self, country_list=None, python_path=None, managepy_path=None, path=None, year_list=None, *args, **options):
        script_path = './export_to_flat.sh'

        if not country_list:
            sys.exit("Please provide a comma separated country_list (e.g. 'AT,BE,LU')")
        country_list = country_list.split(',')
        sys.stdout.write("Working with the following country list: %s\n" % str(country_list))

        if not python_path:
            sys.exit("Please provide the full path to your python interpreter (e.g. '/home/projectenv/venv/python')")
        sys.stdout.write("Working with the following python path: %s\n" % str(python_path))

        if not managepy_path:
            sys.exit("Please provide the full path to your project manage.py file (e.g. '/home/my-project/manage.py')")
        sys.stdout.write("Working with the following manage.py path: %s\n" % str(managepy_path))

        if not path or not os.path.isdir(path):
            sys.exit("Please provide a valid path to store the exported data files")
        sys.stdout.write("Writing exported data to country subfolders in the following path: %s\n" % path)

        if len(country_list) > 1 and year_list:
            sys.exit("A year list can only be provided when exporting data for a single country")
        if year_list:
            year_list = year_list.split(',')
            yl_from_cl = True
        else:
            yl_from_cl = False

        if os.path.isfile(script_path):
            sys.stdout.write("Deleting existing script file: %s" % script_path)
            os.remove(script_path)
        sys.stdout.write("Generating empty script file: %s" % script_path)
        out_file = open(script_path, 'w+')

        for country in country_list:
            sys.stdout.write("\nGenerating script commands for country %s...\n" % country)
            if not yl_from_cl:
                year_list = list(CountryYear.objects.filter(country=country).values_list('year', flat=True))
                sys.stdout.write("Reading year list from DB: %s\n" % str(year_list))
            else:
                sys.stdout.write("Taking year list from CL input: %s\n" % str(year_list))
            country_folder = os.path.join(path, country)
            sys.stdout.write("Generating script command to create country subfolder: %s\n" % country_folder)
            out_file.write('mkdir ' + country_folder + '\n')

            for year in year_list:
                year = str(year)
                sys.stdout.write("Year %s:\n" % year)
                country_file = country + '_Subsidies_' + year + '.csv'
                full_path = os.path.join(country_folder, country_file)
                sys.stdout.write("Generating export command...\n")
                out_file.write('echo "Generating CSV file %s..."\n' %(full_path))
                cmd  = 'echo "COPY (SELECT r.name,r.address1,r.address2,r.zipcode,r.town,'
                cmd += 'p.amounteuro,p.amountnationalcurrency,s.nameenglish,p.year,p.countrypayment '
                cmd += 'FROM data_payment as p,data_recipient as r,data_scheme as s WHERE p.countrypayment=\'' + country + '\' '
                cmd += 'AND p.year=\'' + year + '\' AND p.globalrecipientid=r.globalrecipientid '
                cmd += 'AND p.globalschemeid=s.globalschemeid) TO STDOUT WITH CSV;" | '
                cmd += python_path + ' ' + managepy_path + ' dbshell > ' + full_path + '\n'
                out_file.write(cmd)

        out_file.close()
        sys.stdout.write("Making script file executable...\n")
        os.chmod(script_path, 0755)
        sys.stdout.write("Run generated script file %s for commands to be executed.\n" % script_path)





