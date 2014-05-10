from django.shortcuts import render
from django.shortcuts import get_object_or_404

from web.feeds.models import FeedItems, FeedCategories
from models import Feature


def news_home(request):
    features = Feature.objects.filter(published=True)[:5]
    feed_items = FeedItems.objects.all()[:5]

    return render(
        request,
        'features/news_home.html',
        {
            'features': features,
            'feed_items': feed_items,
        }
    )


def media_list(request, cat='News'):
    category = FeedCategories.objects.get(name=cat)
    feed_items = FeedItems.objects.filter(feed__category=category)

    return render(
        request,
        'features/media_list.html',
        {
            'feed_items': feed_items,
        }
    )


def feature_list(request):
    features = Feature.objects.filter(published=True)
    return render(request,
        'features/feature_list.html',
        {
            'features': features
        }
    )


def feature_detail(request, slug):
    feature = get_object_or_404(Feature, published=True, slug=slug)
    recent_features = Feature.objects.filter(published=True).exclude(slug=slug).order_by('-id')[:5]
    return render(request,
        'features/feature_detail.html',
        {
            'feature': feature,
            'recent_features': recent_features,
        },
    )
