import tweepy
import random
import time

insults = ("shitty {}", "disgusting {}", "terrible, just terrible {}", "{}, absolutely tremendous", \
    "the great shithole of {}", "{}, who would ever want to go there?")

# make the set of places
f = open('places.txt', 'r')
places = set(x.strip() for x in f.readlines())

def getInsult(word):
        return insults[random.randrange(0, len(insults))].format(word)

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

def change(tweet, f, to):

    if f in tweet:
        new_tweet = tweet
        new_tweet = new_tweet.replace(f, to)
        return new_tweet
    else:
        return tweet
        

if __name__ == "__main__":
    # start up API instance
    twitter = TwitterAPI()

    # get recent tweets in a list of strings, each being a tweet
    recent_tweets = [x.text for x in twitter.api.user_timeline(user_id='25073877', count=5)]

    # update each tweet
    for tweet in range(len(recent_tweets)):

        recent_tweets[tweet] = change(recent_tweets[tweet], \
            '#MakeAmericaGreatAgain', '#MakeAmericaShittyAgain')

        recent_tweets[tweet] = change(recent_tweets[tweet], \
            ' he ', ' Obama ')

        recent_tweets[tweet] = change(recent_tweets[tweet], \
            'thank', 'fuck')
        recent_tweets[tweet] = change(recent_tweets[tweet], \
            'Thank', 'Fuck')

        recent_tweets[tweet] = change(recent_tweets[tweet], \
            'nice', 'shitty')
        recent_tweets[tweet] = change(recent_tweets[tweet], \
            'Nice', 'Shitty')

        recent_tweets[tweet] = change(recent_tweets[tweet], \
            '#VoteTrump', '#DontTrump')
        
        recent_tweets[tweet] = change(recent_tweets[tweet], \
            'Trump', 'Drumpf')

        recent_tweets[tweet] = change(recent_tweets[tweet], \
            '!', '?')

        recent_tweets[tweet] = change(recent_tweets[tweet], \
            'America', random.sample(places, 1)[0])
        recent_tweets[tweet] = change(recent_tweets[tweet], \
            'AMERICA', random.sample(places, 1)[0])
        recent_tweets[tweet] = change(recent_tweets[tweet], \
            'america', random.sample(places, 1)[0])

        split_tweet = recent_tweets[tweet].split()
        for word in places:
            for i in range(len(split_tweet)):
                if word.lower() in split_tweet[i].lower():
                    split_tweet[i] = getInsult(split_tweet[i])
        recent_tweets[tweet] = ' '.join(split_tweet)
    # print all the tweets in console
    [print('\n' + x) for x in recent_tweets]

    # tweet each new tweet if it fits the character limit
    for tweet in recent_tweets:
        if len(tweet) <= 140:
            twitter.tweet(tweet)