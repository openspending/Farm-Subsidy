.. FarmSubsidy.org documentation master file, created by
   sphinx-quickstart on Mon Mar 10 13:23:20 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

FarmSubsidy.org - Developer Documentation
=========================================

This documentation is intended for developers who want to help out with the 
`FarmSubsidy.org <http://farmsubsidy.openspending.org>`_ project which aims
to bring transparency to EU farm subsidies and is run by the `OpenSpending <http://openspending.org/>`_ 
community.

Overview
--------
* In the ``Introduction`` section you can find some information about FarmSubsidy.org and some hints  
  where you might want to start reading to get an overview about European Union farm subsidy policy.
* The ``Website`` section is 
  describing the structure of the website and the corresponding source code
  on `GitHub <https://github.com/openspending/Farm-Subsidy>`_. 
* In the ``Scraper`` section people who want to help out can find information on how to write scapers for the 
  different countries. Scrapers for the data are hosted in a separate
  `GitHub repository <https://github.com/openspending/farmsubsidy-scrapers>`_.

.. note::
   This document - especially the definition for new data format starting in 2013 in the ``scraper`` section
   (see: :ref:`scraper_data_format`) is currently in **DRAFT** status, which means that there will be some
   changes in the next weeks. For recent changes see both the ``website changelog`` (:ref:`website_changelog`) and 
   the ``scraper_changelog`` (:ref:`scraper_changelog`).
   
   *This doesn't mean, that you shouldn't write your scraper yet* since life is a long quite (and ever changing)
   river and 80+ percent of your work will be able to be kept. Just be aware that there might be the need
   of some last changes to get everything to work!
   
   For remarks or questions please contact `holgerd77 <https://github.com/holgerd77>`_  on Github (March 15th, 2014).

.. note::
   New **farmsubsidy data** for **2013** should be release around **April/May 2014**.

User Manual
-----------

.. toctree::
   :maxdepth: 2
   
   introduction
   website
   scraper
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

