from django.template import Library, Node

from farmsubsidy.queries import queries
from farmsubsidy import fsconf

register = Library()
def top_recipients(location="EU", number=5):
  
  country = "country:%s" % location
  if location == "EU":
    country = ""
  
  options = {
    'page' : 0,
    'len' : number,
    'collapse_key' : fsconf.index_values['recipient_id_x'],  
  }
  
  results = queries.do_search("%s amount:1000..1000000000" % country, options)
  
  return locals()

register.inclusion_tag('blocks/top_recipients.html')(top_recipients)  