import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup


def parse_file(file):
    soup = BeautifulSoup()
    xml_tree = ET.parse(file)
    tweets = []

    for document in xml_tree.iterfind('documents/document'):
        tweet_text = document.text

        print(tweet_text)

        tweets.append(tweet_text)

    return tweets
