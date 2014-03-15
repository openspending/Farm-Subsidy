.. _scraper:

=======
Scraper
=======

This part of the documentation describes how to write scrapers for the Farmsubsidy project.

How to contribute
=================

There is a separate **GitHub repository** collecting the different **scrapers**:

* https://github.com/openspending/farmsubsidy-scrapers

In the repository there is a **separate folder** for **each scraper**, named by the country code of the
scraper, e.g. ``at`` for Austria:

* https://github.com/openspending/farmsubsidy-scrapers/tree/master/at

There is also a very detailed **Data Overview document** on **Google Docs**. Public data urls are not
up-to-date any more, but make sure to notice the **Data Documentation URLs** at the end of the ``detail view``
sheet:

*  `Data Overview Document (Google Docs) <https://docs.google.com/spreadsheet/ccc?key=0Ajagl3TOC7X_dFlzQ0ljaUxUWVNmNE40TGdweWNlcEE&hl=en#gid=0>`_

For each scraper there is a corresponding issue on GitHub. If you want to help out with a scraper
have a look at the `open issues <https://github.com/openspending/farmsubsidy-scrapers/issues?labels=memberstate&state=open>`_,
see if there is already somebody responsible and drop a note to avoid that there are several
people working on the same scraper in parallel.

.. note::
   Before you write your scraper:
   
   * Check, if there is a **download button** on the data website (I actually didn't when I wrote the
     example scraper! :-))
   * Do some **creative googling** if someone else already has written a scraper for the site!
     If so: try to get in contact and ask if the scraper can be used under an open licence.

Data Sources
============

Data is provided on a country-by-country basis. Mostly you will find a web form where you can filter 
the data by things like year, amount or the region and get back an HTML table with the single payments. 
Sometimes data is also provided in a downloadable format.

Here are some examples:

* `Belgium <http://www.belpa.be/pub/EN/data.html>`_ (just hit *search* button)
* `UK <http://cap-payments.defra.gov.uk/>`_ (get data by searching for amount > 1.000.000)
* `Germany <http://www.agrar-fischerei-zahlungen.de/Suche>`_ (get data by searching for EGFL > 1.000.000)
* `Slovenia <http://www.arsktrp.gov.si/si/o_agenciji/informacije_javnega_znacaja/prejemniki_sredstev/prejemniki_sredstev/>`_ (get data by selecting a sum and search)

You can find the relevant data source on the issue page of a country in the GitHub repo.

.. _existing_data_format:

Format of the existing data files
=================================

To get an idea of how data is structured in the DB have a look at the :ref:`data_model` chapter in the Website
documentation section. 

You can find the data scraped by the old proprietary scrapers in the following folder:

* http://data.farmsubsidy.org

Please download one of the compressed country data files and unpack it, e.g.:

http://data.farmsubsidy.org/AT.tar.bz2

A data package consists of the following files::

	recipient.txt
	scheme.txt
	payment.txt

Due to its size you probably can't open ``recipient.txt`` or ``payment.txt`` with a visual editor
but need an editor like ``vi`` and use it from the command line.

Each file contains the data for the corresponding data model in ``CSV`` format, here are some extracts.
	
Start of a recipient.txt file::

	"recipientId";"recipientIdx";"globalRecipientId";"globalRecipientIdx";"name";"address1";"address2";"zipcode";"town";"countryRecipient";"countryPayment";"geo1";"geo2";"geo3";"geo4";"geo1NationalLanguage";"geo2NationalLanguage";"geo3NationalLanguage";"geo4NationalLanguage";"lat";"lng"
	1;1;"AT1";"AT1";"Adrigan Barbara";;;;;"AT";"AT";"Burgenland";"Lutzmannsburg";;;;;;;;
	2;2;"AT2";"AT2";"Aibler Maria";;;;;"AT";"AT";"Burgenland";"Zillingtal";;;;;;;;
	3;3;"AT3";"AT3";"Allacher Ilse und Matthias";;;;;"AT";"AT";"Burgenland";"Gols";;;;;;;;
	
Complete scheme.txt file::

	"GlobalSchemeId";"nameNationalLanguage";"nameEnglish";"budgetlines8Digit";"countryPayment"
	"AT7";"Öffentliche Lagerhaltung (Intervention)";"Intervention";;"AT"
	"AT2";"Indirect";"Indirect";;"AT"
	"AT1";"Direct";"Direct payments under European Agricultural Guarantee Fund";;"AT"
	
Start of a payment.txt file::

	"paymentId";"globalPaymentId";"globalRecipientId";"globalRecipientIdx";"globalSchemeId";"amountEuro";"amountNationalCurrency";"year";"countryPayment"
	1223535;"AT1223535";"AT317577";"AT317577";"AT5";11733.75;;"2008";"AT"
	1223536;"AT1223536";"AT12327";"AT12327";"AT5";36445.65;;"2008";"AT"
	1223537;"AT1223537";"AT44239";"AT44239";"AT5";82.10;;"2008";"AT"

.. _scraper_data_format:

Scraper Data Format
===================

CSV Format
----------

The new GitHub scrapers will be used to scrape farmsubsidy data for the year ``2013`` and newer and only
have to output a ``payment`` file with a reduced data format and no ``recipient`` and ``scheme`` files.
Please write your scraper so that it will take the ``year`` as an input parameter and writes files like this::

	payment_YEAR.txt

The reduced data format looks like the following::

	"rName";"rAddress1";"rAddress2";"rZipcode";"rTown";"globalSchemeId";"amountEuro";
	"Nordmilch AG";;;;;"D1";15239.34;
	"Emsland-Stärke GmbH";Am Bahnhof 4B;;15938;Golßen;"D2";32305.45;
	...

The scraped data will be loaded into the database with a (yet to be written) Django management command.
Recipient names will be matched against existing recipient names.

The following table describe the single attribute formats.

====================== ===================================== ========= =========
Attribute              Description                           Mandatory Data Type
====================== ===================================== ========= =========
rName                  Name of recipient                     YES       String
rAdress1               Adress field 1 for recipient (Street) NO        String
rAdress2               Adress field 2 for recipient (other)  NO        String
rZipcode               Zipcode of recipient town             NO        String
rTown                  Town of recipient                     NO        String
globalSchemeID         Scheme ID from existing scheme.txt    YES       String
amountEuro             Amount in Euro (1)                    YES(or 2) Float
amountNationalCurrency Amount in national currency (2)       YES(or 1) Float
====================== ===================================== ========= =========

.. note::
   Since the names you scrape will be later matched against the names already existing in the 
   database please make some searches on the Farmsubsidy website and see, how names are formatted
   there. Try to keep names written as they are on the website so matching will be easier
   and double entries will be prevented.

.. note::
   For the scheme ID please take an existing scheme ID from the ``scheme.txt`` file of the
   country (see :ref:`existing_data_format`). If you can't find a fitting scheme ID ask on
   the GitHub issue page and use a temporary schemeID like ``AT-TMP1``.

.. note::
   Please provide either the amount in Euro or in the national currency (e.g. for UK).
   Don't make any implicit conversions, leave field not provided blank!


UTF-8 Encoding
--------------

Please make sure that you use ``UTF-8`` as an encoding for your output file format and keep
recipient data in the original language and characters.

Here are some examples:

* Bólyi Mezőgazdasági Termelő és Kereskedelmi Zrt. (Hungary)
* GREENGROW spółka z ograniczonš odpowiedzialnociš (Poland)
* Südzucker GmbH (Germany)
* Alcoholes Gcía de la Cruz Vega (Spain)

.. _scraper_technology:

Technology
==========

At the moment, the following technologies/programming languages for scrapers are supported:

.. _technology_scrapy:

Python/Scrapy
-------------

Introduction
^^^^^^^^^^^^
Scrapy is a python scraping framework with a lot of built in scraping functionality,
for introductory information see the ``Scrapy`` website:

* `Scrapy <http://scrapy.org/>`_

Installation
^^^^^^^^^^^^
For running a Scrapy spider, please install the Scrapy version from the requirements file:

* Requirements file: `requirements_scrapy.txt <https://github.com/openspending/farmsubsidy-scrapers/blob/master/requirements_python.txt>`_

You can find a Scrapy project deployment in the GitHub repository in the ``scrapy_fs`` folder.
In this deployment, there is already the data structure defined in the ``items.py`` file.

Writing a spider
^^^^^^^^^^^^^^^^
There is a reference implementation for a scrapy spider for the GB website. The spider can be found
at (`Link <https://github.com/openspending/farmsubsidy-scrapers/blob/master/scrapy_fs/scrapy_fs/spiders/gb_spider.py>`_::

	scrapy_fs/scrapy_fs/spiders/gb_spider.py

If you want to write a spider with Scrapy, please add/name your spider in an analog way and write a note
in the root ``gb`` (``COUNTRY_CODE``) directory that the spider is being realized with Scrapy.

A Scrapy spider can be executed like that from the ``scrapy_fs`` directory::

	scrapy crawl GB -a year=YEAR

A ``CSV`` output can be generated like this::

	scrapy crawl GB -a year=2012 -o payment_2012.txt -t csv

.. note::
   Scrapy won't maintain the order of the attributes of the csv file. That's ok.

Python
------
If you have your own preferred way of writing scrapers with ``Python``, you can do that as well.
Then please write your scraper in a form, that it can be executed from the command line.
Add the requirements you need to the global python requirements file:

* Global requirements file: `requirements_python.txt <https://github.com/openspending/farmsubsidy-scrapers/blob/master/requirements_python.txt>`_

.. note::
   If you've written a Python scraper you think can serve as a good starting point for other scrapers and
   can be entered here as a reference implementation, please drop a note!

Ruby
----
You can also write a ``Ruby`` scraper, please also create the scraper in a command line-executable form.

Add your requirements to the global Ruby Gemfile:

* Global Gemfile: `Gemfile <https://github.com/openspending/farmsubsidy-scrapers/blob/master/requirements_python.txt>`_

.. note::
   If you've written a Ruby scraper you think can serve as a good starting point for other scrapers and
   can be entered here as a reference implementation, please drop a note!

Other
-----
If you have another technology you want to use, please ask the person currently responsible for maintaining
the Scrapers (try on GitHub). The reason for limiting the technologies a bit is that all scrapers for the different countries
have to be maintained and an executable environment have to be kept up to be able to run the scraper
from a central location independently from the creators.

.. _scraper_changelog:

Changelog (Scraper)
===================

This changelog deals mainly with the ``data format definition`` for the scrapers (see: :ref:`scraper_data_format`)
and the ``technology supported`` in the scraper repository (see: :ref:`scraper_technology`).

**Changes in version DRAFT1** (2014-03-15)

* Added basic documentation for scraper repository (see: :ref:`scraper`)
* Added documentation for existing data format (see: :ref:`existing_data_format`)
* Added *DRAFT* definition for a new simplified scraper data format (see: :ref:`scraper_data_format`)
* Added section for supported technologies (see: :ref:`scraper_technology`)
* Added ``scrapy_fs`` Scrapy project on GitHub  
  for unified Scrapy scraper development, ``items.py`` file for data format definition, ``pipelines.py`` file
  for basic data format validation (see: `GitHub scrapy_fs directory <https://github.com/openspending/farmsubsidy-scrapers/tree/master/scrapy_fs>`_)
* Added Scrapy reference scraper for ``GB`` (see `gb_spider.py on GitHub <https://github.com/openspending/farmsubsidy-scrapers/blob/master/scrapy_fs/scrapy_fs/spiders/gb_spider.py>`_)
* Documentation about how to execute Scrapy spiders (see: :ref:`technology_scrapy`) 
