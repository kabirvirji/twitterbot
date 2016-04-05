import tweepy
import random
import time
import sys

print(sys.stdout.encoding)
if sys.stdout.encoding != 'cp850':
  sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'cp850':
  sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')

insults = ("shitty {}", "disgusting {}", "terrible, just terrible {}", "{}, absolutely tremendous", \
            "the great shithole of {}", "{} (who would ever want to go there?)")

# make the set of places
f = open('places.txt', 'r')
places = set(x.strip() for x in f.readlines())

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

def getInsult(word):
        return insults[random.randrange(0, len(insults))].format(word)

def change(tweet, f, to, num=None):
    if num is None:
        if f in tweet:
            new_tweet = tweet
            new_tweet = new_tweet.replace(f, to)
            return new_tweet
        else:
            return tweet
    else:
        if f in tweet:
            new_tweet = tweet
            new_tweet = new_tweet.replace(f, to, 1)
            return new_tweet
        else:
            return tweet
        

if __name__ == "__main__":
    # start up API instance
    twitter = TwitterAPI()

    newest_id = twitter.api.user_timeline(count=1)[0].id
    while (True):
        done = False
        while not done:
            try:
                # get recent tweets in a list of strings, each being a tweet
                statuses = twitter.api.user_timeline(user_id='25073877', count=20)
                recent_tweets = [x.text for x in statuses]
                ids = [print(x.id) for x in statuses]

                # update each tweet
                for tweet in range(len(recent_tweets)):
                    if statuses[tweet].id > newest_id:

                        split_tweet = recent_tweets[tweet].split()
                        for word in places:
                            for i in range(len(split_tweet)):
                                if word.lower() in split_tweet[i].lower():
                                    split_tweet[i] = getInsult(split_tweet[i])
                        recent_tweets[tweet] = ' '.join(split_tweet)

                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            '#MakeAmericaGreatAgain', '#MakeAmericaShittyAgain')
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            '#VoteTrump', '#DontTrump')
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            '#TrumpTrain', '#ChuggaChuggaChooChoo')

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
                            'Trump', 'Drumpf')

                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            '!', '?')

                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'America', random.sample(places, 1)[0])
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'AMERICA', random.sample(places, 1)[0].upper())
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'america', random.sample(places, 1)[0])
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            ' US ', ' ' + random.sample(places, 1)[0] + ' ')
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'united states', random.sample(places, 1)[0])
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'United States', random.sample(places, 1)[0])
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'UNITED STATES', random.sample(places, 1)[0].upper())
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'U.S.', random.sample(places, 1)[0])

                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'Ted', 'Ced')
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'Cruz', 'Truz')
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'Lyin', 'Homie G')

                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'Hillary', 'Cillary')
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'Clinton', 'Hlinton')

                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'her', 'her (or his? who knows)', 1)

                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            '@FoxNews', '@FoxNews (foxy ;) )')

                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'wall', 'HUGE FUCKING WALL')

                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'vote', 'give up')

                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'gun', 'gun (pew pew)')
                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'guns', 'guns (pew pew)')

                        recent_tweets[tweet] = change(recent_tweets[tweet], \
                            'Enjoy', 'HAHAHAHA')

                # print all the tweets in console
                for tweet in range(len(recent_tweets)):
                    if recent_tweets[tweet] is not None and \
                            '<undefined>' not in recent_tweets[tweet] and \
                            '\u2019' not in recent_tweets[tweet] and \
                            '\u2013' not in recent_tweets[tweet] and \
                            statuses[tweet].id > newest_id and \
                            len(recent_tweets[tweet]) <= 140:
                        print(recent_tweets[tweet] + '\n')
            except UnicodeEncodeError:
                pass
            else:
                done = True

            # tweet each new tweet if it fits the character limit
            for tweet in range(len(recent_tweets) - 1, -1, -1):
                if statuses[tweet].id > newest_id and len(recent_tweets[tweet]) <= 140:
                    #twitter.tweet(recent_tweets[tweet])
                    print("Tweeted!")
                    time.sleep(30)

            time.sleep(1800)

            newest_id = statuses[0].id
            statuses = twitter.api.user_timeline(user_id='25073877', count=200)
