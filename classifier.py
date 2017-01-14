from nltk.tokenize import TweetTokenizer
import re


# funtcion gets tweet and returns
# list of tokens from that tweet
def tokenize_tweet(tweet):
    tknzr = TweetTokenizer()
    return tknzr.tokenize(tweet)



# function that preprocess the tweets
def preprocessTweet(tweet):

    # convert to lowercase
    tweet = tweet.lower()

    # convert www. or https:// to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)

    # remove additional white spaces if needed
    # tweet = re.sub('[\s]+', ' ', tweet)

    # replaces hashtag words to actual words
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

    return tweet


# reads the tweets
fp = open('file.txt', 'r')
line = fp.readline()

while line:
    processedTweet = preprocessTweet(line)
    print(processedTweet)
    line = fp.readline()

# close the filereader
fp.close()

test_tweet = "This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <--"

print(tokenize_tweet(test_tweet))

