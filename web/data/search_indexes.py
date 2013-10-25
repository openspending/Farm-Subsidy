from haystack import indexes
from .models import Recipient


class RecipientIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name', default="unknown", weight=2)
    country = indexes.CharField(model_attr='countrypayment', default="unknown",
        faceted=True)
    url = indexes.CharField(model_attr='get_absolute_url')
    total = indexes.FloatField(model_attr='total', default=0.0)

    def get_model(self):
        return Recipient
