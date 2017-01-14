import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from nltk.tokenize import wordpunct_tokenize


def parse_file(file):
    xml_tree = ET.parse(file)
    tweets = []

    for document in xml_tree.iterfind('documents/document'):
        tweets.append(__process_tweet(document.text))
    return tweets


def __process_tweet(tweet_html):
    tweet_processed = {}
    soup = BeautifulSoup(tweet_html, 'html.parser')
    all_links = soup.find_all('a')
    users, images, hashtags, links = process_links(all_links)
    tweet_processed['users'] = 1.0 if len(users) > 0 else 0.0
    tweet_processed['images'] = 1.0 if len(images) > 0 else 0.0
    tweet_processed['hashtags'] = 1.0 if len(hashtags) > 0 else 0.0
    tweet_processed['links'] = 1.0 if len(links) > 0 else 0.0

    tweet_text = ''.join(soup.findAll(text=True))
    dot_count, question_count, exclamation_count, ellipsis_count = process_punctuation(tweet_text)
    total_punctuation = dot_count + question_count + exclamation_count + ellipsis_count

    tweet_processed['.'] = dot_count / total_punctuation if total_punctuation > 0 else 0.0
    tweet_processed['?'] = question_count / total_punctuation if total_punctuation > 0 else 0.0
    tweet_processed['!'] = exclamation_count / total_punctuation if total_punctuation > 0 else 0.0
    tweet_processed['...'] = ellipsis_count / total_punctuation if total_punctuation > 0 else 0.0
    return tweet_processed


def process_links(links):
    users = []
    images = []
    hashtags = []
    others = []

    for link in links:
        if link['class'][0] == 'twitter-atreply':
            users.append(link)
        elif link['class'][0] == 'twitter-timeline-link':
            images.append(link)
        elif link['class'][0] == 'twitter-hashtag':
            hashtags.append(link)
        else:
            others.append(link)
    return users, images, hashtags, others


def process_punctuation(text):
    dot_count = 0
    question_count = 0
    exclamation_count = 0
    ellipsis_count = 0

    tokens = wordpunct_tokenize(text)
    for token in tokens:
        if token == '.':
            dot_count += 1
        elif token.count('?') > 0:
            question_count += 1
        elif token.count('!') > 0:
            exclamation_count += 1
        elif token.count('.') > 1:
            ellipsis_count += 1

    return dot_count, question_count, exclamation_count, ellipsis_count

