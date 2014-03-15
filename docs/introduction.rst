============
Introduction
============

Current Situation
=================

`FarmSubsidy <http://farmsubsidy.openspending.org/>`_ is a website that collects the payment data of
the Common Agriculture Policy (CAP) which represents about a third of the EU budget. It was run by 
a group of journalists and activists for the past years. In 2013 the `OpenSpending project <http://openspending.org/>`_
of the `Open Knowledge Foundation <http://okfn.org/>`_ took over responsibility of the website.

Since the old scrapers were proprietary and are not available any more one of the main tasks in the
current situation is to build a new set of scrapers for each country released under an open licence
which can be maintained by the community.

This documentation is intended to give an overview about the requirements for those scrapers so that the
data they provide can be integrated seamlessly and without too much hassle into the existing environment.

So if you want to help, regardless if you are new to Farmsubsidy or if you have already accompanied the project
over the years: your work will be highly appreciated. This is an extremly important topic, and since
there are 28 member states in the European Union there is a good chance that you'll get your favorite country
to write a scraper for! :-)

.. _background:

Background Information
======================

If you need an introduction to the topic of farm subsidies, you can have a look at the 
`Wikipedia article <https://en.wikipedia.org/wiki/Common_Agricultural_Policy>`_ about EU agricultural policiy 
or at the `CAP website from the European Commision <http://ec.europa.eu/agriculture/cap-funding/index_en.htm>`_. 
The wikipedia article is quite long, for an introduction to the structure of the subsidies just read the 
`The CAP today <https://en.wikipedia.org/wiki/Common_Agricultural_Policy#The_CAP_today>`_ section.

The main thing you have to know, is that European agricultural subsidies are divided into two funds. 
*The European Agricultural Guarantee Fund (EAGF)* 
(`Wikipedia > EAGF <https://en.wikipedia.org/wiki/European_Agricultural_Guarantee_Fund>`_) 
is for direct payments for farmers (majority of payments) and for measures to respond to market disturbances. 
You will find these two posts separately distinguished in the data provided.

The second fund is the *European Agricultural Fund for Rural Development (EAFRD)* 
(`Wikipedia > EAFRD <https://en.wikipedia.org/wiki/European_Agricultural_Fund_for_Rural_Development>`_).

Since EU funding changed over time, there were other so called ``schemes`` of payment though and are also
still today, have a look at the :ref:`scheme` description in the data model chapter.

Further Reading
===============

If you want to do some further reading, here are some sources to start:

* `News section <http://farmsubsidy.openspending.org/news/>`_ on the Farmsubsidy website
* Googling `"farm subsidies EU" <https://www.google.com/?gfe_rd=ctrl&ei=gyokU7aGMsOvtQbvhIGICQ&gws_rd=cr#q=farm+subsidies+eu>`_
* Same on `Google News <https://www.google.com/?gfe_rd=ctrl&ei=gyokU7aGMsOvtQbvhIGICQ&gws_rd=cr#q=farm+subsidies+eu&tbm=nws>`_ 



