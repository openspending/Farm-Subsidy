# Farmsubsidy.org

This code runs farmsubsidy.openspending.org. Please read INSTALL for installation instructions.

If you are interested in the project in general, please contact the [OpenSpending Team](http://openspending.org/about/contact.html).

## Developer Documentation

More extensive developer documentation is just being build up at http://farmsubsidy.readthedocs.org.


## Installation

Follow instructions in `INSTALL.txt`.


## Loading data

These management commands load data for specific country. The data must be located in the data folder like this `data/<CountryCode>/payment.txt`. You need `payment.txt`, `recipient.txt` and `scheme.txt` files.

## Import fresh data

E.g. for Austria:

    python manage.py copier -c AT
    python manage.py normalize -c AT

Repeat for every country.

Run a `VACUUM VERBOSE ANALYZE` on all database tables afterwards.

After all countries are imported, run search indexing:

    python manage.py fs_update_index


After this you can update the total payments number on the front page like this:

    python manage.py payment_totals
