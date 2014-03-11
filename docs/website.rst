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
   
Create a copy ``settings.py`` from ``settings.py.template`` and adopt the settings to your needs (for a test
deployment maybe use ``SQLite`` instead of ``PostgreSQL`` e.g., though this depends if you want to play
with larger amounts of data).

4) Sync/migrate the DB
^^^^^^^^^^^^^^^^^^^^^^

Since there is an old ``GeoDjango`` dependency in the ``South`` migrations, early migrations won`t work
without hassle, so sync all apps with ``syncdb``::

	cd web
	python manage.py syncdb --all
	
For getting ``South`` back to work again, first list all apps which uses migrations::
	
	python manage.py migrate --list
	
Then do fake migrations to the latest migration for all apps, e.g.::
	
	python manage.py migrate data LATESTMIGRATIONNUMBER --fake

5) Install Haystack backend
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you use ``Whoosh`` as a backend for Haystack, you have to install it (older version due to dependencies)::

	pip install whoosh==2.4

6) Temporary: create payment_totals.txt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is due to some legacy code and will be removed as soon as possible:

Create a textfile ``data/stats/payment_totals.txt`` (from repository root, not from ``web`` directory)
and enter some fake numbers like this::

	1000000,100000

7) Run the server
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