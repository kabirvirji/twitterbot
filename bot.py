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

firstnouns = ("Donald Trump", "Hilary Clinton", "Bernie Sanders", "Ted Cruz", "Person of colour")
verbs = ("subjected", "hits a", "jumps on", "drives", "barfs on", "burns", "practices") 
secondnoun = ("themself", "a confederate flag", "racism", "female", "monkey", "Donald Trump")
adv = ("crazily.", "stupidly.", "foolishly.", "fantastically.", "occasionally.")

random_sentance = '@realDonaldTrump'

num = random.randrange(0, len(firstnouns))
random_sentance += firstnouns[num] + ' '
num = random.randrange(0,len(verbs))
random_sentance += verbs[num] + ' '
num = random.randrange(0,len(secondnoun))
random_sentance += secondnoun[num] + ' '
num = random.randrange(0,len(adv))
random_sentance += adv[num] + ' '
num = random.randrange(0,len(adj))
        

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet(random_sentance)