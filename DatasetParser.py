import xml.etree.ElementTree as ET


def parse_file(file):
    xml_tree = ET.parse(file)
    tweets = []

    for document in xml_tree.iterfind('documents/document'):
        tweet_text = document.text
        tweets.append(tweet_text)

    return tweets
