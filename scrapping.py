from bot import TwitterAPI

def create_word_dict(tweets):
	"""
	Return a dictionary from the given list of tweets (str).

	Step 1: Create a list of JUST characters for each tweet.
	Step 2: Count each word and place stats in a dict.

	@type tweets: list[str]
	@rtype: dict{str:int}
	"""
	print(len(tweets))
	# step 1
	split_tweets = recent_tweets[:]
	for tweet in split_tweets:
		temp_list = tweet.split()
		for string in temp_list:
			temp_string = ''
			for char in string:
				if char.isalnum():
					temp_string += char.lower()
			temp_list[temp_list.index(string)] = temp_string
		split_tweets[split_tweets.index(tweet)] = temp_list
	
	# step 2
	tweet_dict = {}
	for tweet in split_tweets:
		for word in tweet:
			if word in tweet_dict:
				tweet_dict[word] += 1
			else:
				tweet_dict[word] = 1

	popular_dict = tweet_dict.copy()
	for word in tweet_dict:
		if tweet_dict[word] < 50:
			popular_dict.pop(word)
	print (popular_dict)

if __name__ == '__main__':
	twitter = TwitterAPI()
	recent_tweets = [x.text for x in twitter.api.user_timeline(user_id='25073877', count=30000)]
	create_word_dict(recent_tweets)