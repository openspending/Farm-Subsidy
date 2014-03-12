=======
Scraper
=======

This part of the documentation describes how to write scrapers for the Farmsubsidy project.

How to contribute
=================

There is a separate **GitHub repository** collecting the different **scrapers**:

* https://github.com/openspending/farmsubsidy-scrapers

In the repository there is a separate folder for each scraper, named by the country code of the
scraper, e.g. ``at`` for Austria:

* https://github.com/openspending/farmsubsidy-scrapers/tree/master/at

For each scraper there is a corresponding issue on GitHub. If you want to help out with a scraper
have a look at the `open issues <https://github.com/openspending/farmsubsidy-scrapers/issues?labels=memberstate&state=open>`_,
see if there is already somebody responsible and drop a note to avoid that there are several
people working on the same scraper in parallel.

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


Existing Data Format
====================

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


Scraper Data Format
===================

The new GitHub scrapers will be used to scrape farmsubsidy data for the year ``2013`` and newer and only
have to output a ``payment`` file with a reduced data format and no ``recipient`` and ``scheme`` files.
Please write your scraper so that it will take the ``year`` as an input parameter and writes files like this::

	payment_YEAR.txt

The reduced data format looks like the following::

	"rName";"rAddress1";"rAddress2";"rZipcode";"rTown";"globalSchemeId";"amountEuro";
	"Nordmilch AG";;;;;"D1";15239.34;
	"Emsland-Stärke GmbH";;;;;"D2";32305.45;
	...

The scraped data will be loaded into the database with a (yet to be written) Django management command.
Recipient names will be matched against existing recipient names.

The following paragraphs describe the single attribute formats.

recipientName
^^^^^^^^^^^^^

TODO

Scheme Selection
================

To make things more fun, you often have local abbreviations for the names of the funds 
(e.g. *ELER* in german for the *EAFRD* fund). One tip: sometimes Google Translate 
(use Google Chrome for direct translation) can help to translate even the abbreviation back on the local sites. 
You can (normally) also distinguish the two funds by - like said above - having two posts for the *EAGF* and 
only one for the *EAFRD*.





