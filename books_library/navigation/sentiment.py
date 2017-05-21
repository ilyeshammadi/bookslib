import json

import requests

POSITIVE = 'pos'
NEGATIVE = 'neg'
NEUTRAL = 'neutral'

def get_sentiment(text):
    try:
        res = requests.post('http://text-processing.com/api/sentiment/',
                            data={'text': text})
        if res.status_code == 200:
            sentiment = json.loads(res.content)
            return sentiment['label']
    except:
        return NEUTRAL
