from haystack import indexes
from features.models import Feature


class FeatureIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    published = indexes.BooleanField(model_attr='published', default=False)

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(published=True)

    def get_model(self):
        return Feature
