from haystack.indexes import SearchIndex, CharField
from haystack import site
from models import List


class ListIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    name = CharField(model_attr='name', weight=2)

site.register(List, ListIndex)
