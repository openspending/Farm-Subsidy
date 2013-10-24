from haystack import indexes
from .models import Recipient


class RecipientIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name', default="unknown", weight=2)
    country = indexes.CharField(model_attr='countrypayment', default="unknown",
        faceted=True)

    def get_model(self):
        return Recipient
