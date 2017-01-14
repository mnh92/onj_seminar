import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup


def parse_file(file):
    xml_tree = ET.parse(file)
    tweets = []

    for document in xml_tree.iterfind('documents/document'):
        tweets.append(__process_tweet(document.text))
        break

    return tweets


def __process_tweet(tweet_text):
    tweet_processed = {}
    soup = BeautifulSoup(tweet_text, 'html.parser')
    all_links = soup.find_all('a')
    users, images, hashtags, links = __process_links(all_links)
    tweet_processed['users'] = 1.0 if len(users) > 0 else 0.0
    tweet_processed['images'] = 1.0 if len(images) > 0 else 0.0
    tweet_processed['hashtags'] = 1.0 if len(hashtags) > 0 else 0.0
    tweet_processed['links'] = 1.0 if len(links) > 0 else 0.0

    return tweet_processed


def __process_links(links):
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