import DatasetParser as dp

# example file
with open('example_data/0a9e35fd6f123137d585a482f2484d8e.xml', 'r') as file:
    instances = dp.parse_file(file)

# example processed tweet
tweet_example = {}
tweet_example['images'] = 0.0
tweet_example['users'] = 1.0
tweet_example['links'] = 1.0
tweet_example['.'] = 0.0
tweet_example['!'] = 0.5
tweet_example['?'] = 0.0
tweet_example['...'] = 0.34
tweet_example['female'] = True
