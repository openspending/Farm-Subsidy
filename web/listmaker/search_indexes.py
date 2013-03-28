from haystack import indexes
from models import List


class ListIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name', weight=2)

    def get_model(self):
        return List
