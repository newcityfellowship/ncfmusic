from django.utils.text import truncate_words
from django.utils.html import strip_tags
from django.conf import settings
from twitter import Api, TwitterError, Status

import socket, sys

CHARACTER_LIMIT = 140

class BetterApi(Api):
    def BetterPostUpdate(self, status, data={}):
        """
            Allows for passing in other data for post
        """
        if not self._oauth_consumer:
            raise TwitterError("The twitter.Api instance must be authenticated")
        
        url = '%s/statuses/update.json' % self.base_url
        
        if isinstance(status, unicode) or self._input_encoding is None:
            u_status = status
        else:
            u_status = unicode(status, self._input_encoding)
        
        data.update({'status': status})
        json = self._FetchUrl(url, post_data=data)
        
        data = self._ParseAndCheckTwitter(json)
        
        return Status.NewFromJsonDict(data)
    
    def GetConfig(self):
        url = '%s/help/configuration.json' % self.base_url

        json = self._FetchUrl(url)
        data = self._ParseAndCheckTwitter(json)
        return data

def update_twitter(status, url):
    api = Api(consumer_key=settings.TWITTER_CONSUMER_KEY,
                    consumer_secret=settings.TWITTER_CONSUMER_SECRET,
                    access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY,
                    access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET
                    )
    config = api.GetHelpConfiguration()
    short_url_length = config['short_url_length']

    #   Trim the status back to CHARACTER_LIMIT - short_url_length - 10 (for space between and hash tag)
    status_length = CHARACTER_LIMIT - short_url_length - 10

    status = '%s http://%s%s' % (status, 'http://ncfmusic.com', url)

    try:
        status = api.PostUpdate(status)
    except TwitterError, e:
        sys.stderr.write('TWITTER ERROR: %s: %s\n' % (e, status))
        pass