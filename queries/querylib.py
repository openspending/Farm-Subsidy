#!/usr/bin/env python
# encoding: utf-8
"""
querylib.py

Created by Sym on 2009-02-25.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.

This module should:

Provide:

* A xapian database opject for queries
* A xapian enquire opject

"""

import sys
import os
import xapian
sys.path.append('../indexer') # FIXME: Do this better!
import fsconf

import mappings

def load_database(db=fsconf.xapianDbPath):
  """Returns a xapian.Database object
  
  - `db` full path to a xapian database
  
  """

  db = xapian.Database(db)
  return db


def load_enquire(db):
  """returns a xapian.Enquire opject
  
  - `db` a xapian.Database object
  
  """

  enquire = xapian.Enquire(db)
  return enquire


def load_queryparser():
  """Creates a xapian.queryparser object and creates the default term prefixes and value range searchers."""

  qp = xapian.QueryParser()
  field_mappings = mappings.fieldTypeMaps()
  qp.set_default_op(xapian.Query.OP_AND)
  vasd = xapian.NumberValueRangeProcessor(1,'name')
  qp.add_valuerangeprocessor(vasd) 
  
  for key,field in field_mappings.items():
    # field = mappings[key]
    # print field
    # sys.exit()
    # field = mappings[field]

    if 'value_range_search' in field:
      # vrp = xapian.NumberValueRangeProcessor(field['value'],field['value_range_prefix'])
      try:
        vasd = xapian.NumberValueRangeProcessor(1,'name')
        qp.add_valuerangeprocessor(vasd) 
        vrp = None
      except Exception, e:
        print e

    if 'prefix' in field:
      if 'boolean' in field:
        qp.add_boolean_prefix(field['name'], field['prefix'])
      else:
        qp.add_prefix(field['name'], field['prefix'])
      
  return qp


def format_range_query(valuerange):
  """Ensures any valueRange query is formatted in the x..x format"""
  if len(valuerange.split('..')) < 2:
    return "%s..%s" % (valuerange, valuerange)
  else:
    return valuerange
    
  
def parse_query(query):
  """takes a query string and does any cleaning needed."""
  # query = query.split(' ')




  # 
  # for term in query:
  #   try:
  #     (k,v) = term.split(':')
  #     if k in payment_keys:
  #       if payment_keys[k] == "range":
  #         v = format_range_query(v)
  #       payments.append("%s:%s" % (k,v))
  #     else:
  #       recipients.append("%s:%s" % (k,v))
  #   except:
  #     recipients.append(term)
  # 
  return query
  
  
if __name__ == "__main__":
  db = load_database()
  print db.get_description()
  eq = load_enquire(db)
  
  
  
  