from haystack import indexes
from .models import Recipient


class RecipientIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name', weight=2)
    country = indexes.CharField(model_attr='countrypayment', faceted=True)
    url = indexes.CharField(model_attr='get_absolute_url', indexed=False)
    total = indexes.FloatField(model_attr='total', default=0.0, indexed=False)

    def get_model(self):
        return Recipient

    def index_queryset(self, using=None):
        return self.get_model().objects.exclude(total=None)
