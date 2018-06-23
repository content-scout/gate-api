import json

from django.conf import settings
from django.core.management import BaseCommand
import tweepy

import SeizureChecker.twitter_settings


class Command(BaseCommand):
    def authenticate(self):
        auth = tweepy.OAuthHandler(
            settings.CONSUMER_KEY,
            settings.CONSUMER_SECRET
        )

        auth.set_access_token(
            settings.ACCESS_TOKEN,
            settings.ACCESS_SECRET
        )

        api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
        return api


    def get_search_results(self, api):
        query_string = 'epilepsy'
        results = api.search(query_string, lang='en')
        print('Got {} results'.format(len(results)))

        return results


    def handle(self, *args, **kwargs):
        api = self.authenticate()
        results = self.get_search_results(api)

        with open('results.json', 'w') as file:
            json.dump(results, file)
