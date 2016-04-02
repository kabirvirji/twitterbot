import tweepy
import random
import time

tweetSpeed = 20

firstnouns = ("Donald Trump", "Hilary Clinton", "Bernie Sanders", "Ted Cruz", "Person of colour", \
                "Anonymous", "A Fox News Reporter")
verbs = ("subjected", "hits", "jumps on", "drives", "barfs on", "burns", "practices") 
secondnoun = ("themself", "a confederate flag", "racism", "a female", "an eagle", "Donald Trump", \
                "Hilary Clinton", "Anonymous", "a Donald Trump protester")
adv = ("crazily.", "stupidly", "foolishly", "fantastically", "occasionally", \
                "for probably a good amount of the day", "arrogantly", "awkwardly", "compassionately", \
                "cunningly", "emotionally", "greedily", "kindheartedly", "lovingly", "occasionally", \
                "passionately", "respectfully", "ruthlessly", "subtly", "wiggly")

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

    def trumpTrumpXTimes (self, x):
        if x == '-1':
            while (true):
                random_sentance = '@realDonaldTrump '

                # add the first noun which is always a person
                num = random.randrange(0, len(firstnouns))
                random_sentance += firstnouns[num] + ' '
                # what is this person doing?
                num = random.randrange(0,len(verbs))
                random_sentance += verbs[num] + ' '
                # and to what/who is this person doing that thing?
                num = random.randrange(0,len(secondnoun))
                random_sentance += secondnoun[num] + ' '
                ifAdv = random.randrange(0,2)
                # add an adverb only sometimes
                if ifAdv == 0:
                    num = random.randrange(0,len(adv))
                    random_sentance += adv[num]
                random_sentance += '.'

                # tweet the sentence
                twitter.tweet(random_sentance)
                # wait a minute then go again
                time.sleep(tweetSpeed)
        else:
            for i in range(x):
                random_sentance = '@realDonaldTrump '

                # add the first noun which is always a person
                num = random.randrange(0, len(firstnouns))
                random_sentance += firstnouns[num] + ' '
                # what is this person doing?
                num = random.randrange(0,len(verbs))
                random_sentance += verbs[num] + ' '
                # and to what/who is this person doing that thing?
                num = random.randrange(0,len(secondnoun))
                random_sentance += secondnoun[num] + ' '
                ifAdv = random.randrange(0,2)
                # add an adverb only sometimes
                if ifAdv == 0:
                    num = random.randrange(0,len(adv))
                    random_sentance += adv[num]
                random_sentance += '.'

                # tweet the sentence
                twitter.tweet(random_sentance)
                print (x, 'times tweeted')
                # wait a minute then go again
                time.sleep(tweetSpeed)
        

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.trumpTrumpXTimes(2)