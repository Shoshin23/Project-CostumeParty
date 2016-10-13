from haystack import indexes

from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    location = indexes.CharField(model_attr='location')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Post

    def index_queryset(self,using=None):
        return self.get_model().objects.all()
