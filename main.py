import DatasetParser as dp
import os, random


# example file
with open('example_data/0a9e35fd6f123137d585a482f2484d8e.xml', 'r') as file:
    instances = dp.parse_file(file)


# path to folder with data
folder = 'pan16-author-profiling-training-dataset-english-2016-04-25'


# randomly divide dataset into two datasets:
# training dataset contains 90% of data and
# test dataset contains remaining 10%


# list with all the randomly selected files from folder
testing = []

# list with all the names of files in folder
training = os.listdir(folder)
training.remove("truth.txt")
print(len(training))


num_test = int(len(training) * 0.1)
print(num_test)

for i in range(num_test):
    # randomly select one file and add it to test list
    testing.append(random.choice(training))
    # then remove it from training list
    training.remove(random.choice(training))


# print(training)
# print(len(training))
# print(testing)
# print((len(testing)))

