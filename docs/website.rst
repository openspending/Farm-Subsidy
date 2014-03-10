=======
Website
=======

Installation
============

Requirements
------------

TODO

Installation process
--------------------

1) Git clone the project:

2) Set up a virtualenv and install pip::

	virtualenv --no-site-packages .
	source bin/activate
	pip install -r requirements.txt

3) Set up Django::

	cd web
	python manage.py syncdb --migrate

Post-installation hacks
-----------------------

Execute the following SQL manually in case your columns don't fit (it can't be migrated)::

	ALTER TABLE data_recipient ALTER COLUMN total SET DEFAULT 0.0;
	ALTER TABLE data_countryyear ALTER COLUMN total SET DEFAULT 0.0;
	ALTER TABLE data_recipientyear ALTER COLUMN total SET DEFAULT 0.0;
	ALTER TABLE data_scheme ALTER COLUMN total SET DEFAULT 0.0;
	ALTER TABLE data_schemeyear ALTER COLUMN total SET DEFAULT 0.0;
	ALTER TABLE data_recipientschemeyear ALTER COLUMN total SET DEFAULT 0.0;
	ALTER TABLE data_totalyear ALTER COLUMN total SET DEFAULT 0.0;

It's needed to make ``total`` columns default to ``0.0``.

Data Model
==========

Structure
---------

TODO

Loading data
------------

These management commands load data for specific country. The data must be located in the data folder 
like this ``data/<CountryCode>/payment.txt``. You need ``payment.txt``, ``recipient.txt`` and ``scheme.txt`` files.

Import fresh data
-----------------

E.g. for Austria::

    python manage.py copier -c AT
    python manage.py normalize -c AT

Repeat for every country.

Run a ``VACUUM VERBOSE ANALYZE`` on all database tables afterwards.

After all countries are imported, run search indexing::

    python manage.py fs_update_index


After this you can update the total payments number on the front page like this::

    python manage.py payment_totals

Testing
=======

Test coverage is poor, but new tests are being written all the time, as my resolution is not to fix any 
bug without writing a test for it first.

Some tests only test code, but mostly the tests are there for making sure the database is being processes 
correctly in the (de)normalization process.

Because there is quite a large dataset (to make testing better) it's highly recommended that a persistent 
test database is set up and the `persistent test runner <http://readthedocs.org/docs/django-test-utils/en/0.3/keep_database_runner.htm>`_ 
from Django Test Utils is used.

The initial data for the recipient, payment and scheme model is found in ``./web/data/fixtures/data.sql``.
This should be loaded in to the ``test_[db_name]`` database before running the tests.

Below are the steps that should be taken, assuming the code is actually running:

1) Install ``django-test-utils`` and append ``test_utils`` to ``INSTALLED_APPS`` in ``settings.py`` (see comment there)

2) Create the test database somehow. I find this is easiest done by running ``./manage.py testserver`` as this 
   doesn't destroy the database on exit. You could also prefix the database name in settings 
   with ``test_``, syncdb and then change it back again.

3) Load the data in ``./web/data/fixtures/data.sql`` in to the new database. This isn't added automatically
   because of the time it takes to run tests without the persistent database.

4) run ``./manage.py quicktest``