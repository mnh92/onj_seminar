from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer




#tekst pretvori v tage in izracuna sentiment (pozitiven/negativen)
blob = TextBlob("Test te knjiznice!", analyzer=NaiveBayesAnalyzer())

print(blob)
print(blob.sentiment)