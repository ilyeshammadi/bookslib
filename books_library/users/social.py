import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'auYS8IWtVrGYzfLngBjhfR3jT'
consumer_secret = 'eY3TQzpsdrb74znfN4V80mtcK2n0YA36o7GWcZqFLbqCFpprWp'
access_token = '4244605367-uBSzPDdnbLLVpropRgV1UBs3IURxvcsZr0vtrho'
access_token_secret = 'yclXtFvvUi5FobPq0tn9ecAnmKef5UhV4TZVu6K4nTFLX'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def get_tweets(username):
    for status in tweepy.Cursor(api.user_timeline, screen_name='@{0}'.format(username)).items(20):
        yield status._json['text']
