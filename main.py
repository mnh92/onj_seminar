import Tester
import random, os

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
# print(len(training))


num_test = int(len(training) * 0.1)
# print(num_test)

for i in range(num_test):
    # randomly select one file from training set
    random_file = random.choice(training)

    # append that file to testing set
    testing.append(random_file)

    # then remove that same file from training set
    training.remove(random_file)


# print(training)
# print(len(training))
# print(testing)
# print((len(testing)))

folder = 'pan16-author-profiling-twitter-downloader/pan16-author-profiling-training-dataset-english-2016-04-25'
tester = Tester.Tester(folder)
tester.run_evaluation()

