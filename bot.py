import tweepy
import random

class TwitterAPI:
    def __init__(self):
        consumer_key = "WhLHy9vrJkUcUxwk4yMzVCBHv"
        consumer_secret = "vMFE8YA3FjeNhhVRiyy4agCjxQexHKjzXyJC7AIWrIkc0FWrLs"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "716345350626394112-7ueuLKPYAMTYzZ14Of0iusdaqB59ATs"
        access_token_secret = "0tgfufNwO0GOfQt4KBS7ivhIVfDYvGKqMyl50u4pWU8Vh"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs") 
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")
num = random.randrange(0,5)

random_sentance = '@DonaldJTrump' + nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num]
        

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet(random_sentance)