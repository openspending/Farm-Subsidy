from datetime import datetime
from django.conf import settings
from django.core.cache import cache
import twitter

def latest_tweet( request ):
    tweet = cache.get( 'tweet' )

    # if tweet:
    # return {"tweet": 'tweet'}
    try:
      t = twitter.Twitter()
      tweet = t.statuses.user_timeline(id='farmsubsidy')[0]
      # tweet.date = datetime.strptime( tweet.created_at, "%a %b %d %H:%M:%S +0000 %Y" )
      cache.set( 'tweet', tweet, settings.TWITTER_TIMEOUT )
    
      return {"tweet": tweet}
    except Exception, e:
      if settings.DEBUG:
        return {"tweet" : e}
      else:
        return {"tweet" : ''}
      