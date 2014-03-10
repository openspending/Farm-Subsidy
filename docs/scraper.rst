=======
Scraper
=======


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

To make things more fun, you often have local abbreviations for the names of the funds 
(e.g. *ELER* in german for the *EAFRD* fund). One tip: sometimes Google Translate 
(use Google Chrome for direct translation) can help to translate even the abbreviation back on the local sites. 
You can (normally) also distinguish the two funds by - like said above - having two posts for the *EAGF* and 
only one for the *EAFRD*.


Data Format
===========

General exchange format will be CSV. Past data is available at http://data.farmsubsidy.org.

Requirements for scrapers are not yet determined. A likely format is just a unix program that outputs scraped CSV.


