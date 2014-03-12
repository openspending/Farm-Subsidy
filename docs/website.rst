=======
Website
=======

This is the developer documentation for the **Farmsubsidy website**, located under the following url:

* http://farmsubsidy.openspending.org

**Sources** for the website can be found on **GitHub**:

* https://github.com/openspending/Farm-Subsidy/

The website is build with ``Python`` using ``Django`` as a web framework.

Installation
============

Requirements
------------

The following list contains only the most central requirements to get an overview
which software components are used. For a complete overview have a look at the
`requirements.txt <https://github.com/openspending/Farm-Subsidy/blob/master/requirements.txt>`_ file on GitHub.

* `Django <https://www.djangoproject.com/>`_ 1.5.x
* `Haystack <http://haystacksearch.org/>`_ 2.0.x for search (`GitHub Fork <https://github.com/stefanw/django-haystack/tree/farmsubsidy-deploy>`_ with modifications)
* `django-registration <https://bitbucket.org/ubernostrum/django-registration/>`_ for user login
* `django-piston <https://bitbucket.org/jespern/django-piston/wiki/Home>`_ for the API

The website uses ``South`` for DB migrations/changes:

* `South <http://south.aeracode.org/>`_


Installation process
--------------------

1) Get a copy of the project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

Git clone the project::

	git clone git@github.com:openspending/Farm-Subsidy.git #or use https

2) Install requirements
^^^^^^^^^^^^^^^^^^^^^^^

Set up ``virtualenv`` and ``pip`` and install the requirements::

	virtualenv venv
	source venv/bin/activate
	pip install -r requirements.txt


3) Configure Django
^^^^^^^^^^^^^^^^^^^

The Django project is located in the ``web`` folder.

The Django ``settings.py`` file is split into two separate files. ``global_settings.py`` contains
settings which shouldn't change in a deployment, ``settings.py.template`` contains settings which
should be adopted in a new deployment.
   
Create a copy ``settings.py`` from ``settings.py.template`` and adopt the settings to your needs.

4) Install PostgreSQL
^^^^^^^^^^^^^^^^^^^^^

Farmsubsidy code uses some ``SQL`` syntax which is not compatible with ``SQLite`` and the website
is intended to handle/present large amounts of data, so you have to start directly with a native
DB and ommit a test installation with ``SQLite``. Since Farmsubsidy is build and tested with ``PostgreSQL``,
a ``PostgreSQL`` installation is recommended.

If you haven't that much experience with installing databases: it's not as painful as you might
think, for the mac e.g. there is a client which can be installed and is up and running with one click:
http://postgresapp.com/

Open ``psql`` and create a new DB with::

	CREATE DATABASE farm_geo; 

If you are just running a test installation on localhost not using a username and passwort (don't do that
in production) this should already do the trick!

5) Sync/migrate the DB
^^^^^^^^^^^^^^^^^^^^^^

Since there is an old ``GeoDjango`` dependency in the ``South`` migrations, early migrations won`t work
without hassle, so sync all apps with ``syncdb``::

	cd web
	python manage.py syncdb --all
	
For getting ``South`` back to work again, first list all apps which uses migrations::
	
	python manage.py migrate --list
	
Then do fake migrations to the latest migration for all apps, e.g.::
	
	python manage.py migrate data LATESTMIGRATIONNUMBER --fake

6) Install Haystack backend
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you use ``Whoosh`` as a backend for Haystack, you have to install it (older version due to dependencies)::

	pip install whoosh==2.4

7) Temporary: create payment_totals.txt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is due to some legacy code and will be removed as soon as possible:

Create a textfile ``data/stats/payment_totals.txt`` (from repository root, not from ``web`` directory)
and enter some fake numbers like this::

	1000000,100000

8) Run the server
^^^^^^^^^^^^^^^^^

Run the development server with::

	python manage.py runserver

You should be able to see the farm subsidy website under the URL provided and enter the admin area.

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

Source Overview
===============

Apps
----
Like all Django projects the Farmsubsidy website is organized in different Django apps.
Here is a list of the existing apps with a short description. Don't take the *Importance*
column too serious, it is just for rough orientation:

=========== ================================= =============== ============== ==========
App         Description                       URL paths       Status         Importance
=========== ================================= =============== ============== ==========
api         API for farmsubsidy               /api/           inactive       \+
comments    
countryinfo App for transparency index        /transparency/  active         ++
data        **Central app, data structure**   /, /ES/*        active         +++                                                
features    News and reports app              /news/*         active         \+
feeds
frontend    Annotation management for users   /myaccount/*    active         \+
graphs      Graph visualisation               /graph/*        inactive       o
listmaker   Experimental, recipient lists     /lists/*        inactive       \+
petition    Special petition app, ignore      /petition/*     inactive       o
search      Haystack search                   /search/*       active         ++
=========== ================================= =============== ============== ==========

Other folders:

=========== =====================================================
Folder      Description
=========== =====================================================
locale      Minimal french localization file, ignore
media       CSS, images and Javascript 
misc        Small helper classes and functions
templates   Central folder for all templates
=========== =====================================================



Loading Data
============

.. _data_model:

Data model
----------

You can find the main data structure in the 
`models.py file <https://github.com/openspending/Farm-Subsidy/blob/master/web/data/models.py>`_ 
of the ``data`` app.

The core models are:

Recipient
^^^^^^^^^
A ``recipient`` is a receiver of subsidy payments and is in most cases a company or governmental 
institution.

There are no unique recipient IDs provided by the EU, so the IDs are provided internally by
the system. The central identifying attribute for the recipient is the ``name`` attribute,
though there will sometimes be double entries for the same entities due to inconsistencies in
the source data.

Most other information like adress data or geo information is not mandatory.

Scheme
^^^^^^
A ``scheme`` is identifying a type of payment. Since the structure of the EU subsidy system has
changed over the years you can also find different type of schemes for the payments, examples are:

* Export subsidies
* Market regulations
* School Milk (yeah, healthy :-))
* ...

In the last years, the dominating schemes are:

* European Agricultural Fund for Rural Development (EAFRD)
* Direct payments under European Agricultural Guarantee Fund (EAGF direct)
* Other payments under European Agricultural Guarantee Fund (EAGF other)

See also the :ref:`background` chapter for where to read about this.

Payment
^^^^^^^
A ``payment`` is a paid subsidy for a certain ``recipient`` connected with an existing ``scheme`` for 
a special year. There can be several payments per year for different schemes for the same recipient.


Download the data
-----------------

Data for Farmsubsidy in ``CSV`` format can be found here:

* http://data.farmsubsidy.org

This is not necessarily the newest data available but should do it for test purposes.
Data for a single country is provided in a packaged format, e.g.:

* http://data.farmsubsidy.org/AT.tar.bz2

Put the data in the data folder in the following format::

	data/csv/<CountryCode>/payment.txt

You need the following files there:

* ``payment.txt``
* ``recipient.txt``
* ``scheme.txt``

Import the data
---------------

Now you can import the data with custom Django management commands, e.g. for Austria::

    python manage.py copier -c AT #takes some time...
    python manage.py normalize -c AT #takes even longer...

Repeat that for every country or test with data for just one country.

Run a ``VACUUM VERBOSE ANALYZE`` on all database tables afterwards (make sure you are
connected to the correct database before, on ``psql``: ``\c farm_geo``).

Now you should be able to browse the imported data on the local website and see the list
of ``recipients`` in the Django admin area.

Update the search index
-----------------------

When all/some countries are imported, run search indexing::

    python manage.py fs_update_index
    
    #yes, you guessed it, don't drink too much coffee :-)...
    #For this step you can definitely go away and do something else.

Now you should be able to use the search box on the website and get some results.

Update total payments number
----------------------------

After this you can update the total payments number on the front page like this::

    python manage.py payment_totals #This is quick. Whew. :-)

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