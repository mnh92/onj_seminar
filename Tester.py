import DatasetParser as dp
import os, random
import Classifier
import numpy as np
import re
import time


class Tester:

    def __init__(self, folder):
        self.folder = folder

    def run_evaluation(self):
        start = time.time()

        print('Evaluation start')
        training, testing = self.__split_data()

        print('preparing training data...')
        training_data, target_vector = self.__prepare_training_data(training)
        classifier = Classifier.Classifier()

        train_start = time.time()
        print('training model...')
        classifier.train_model(training_data, target_vector)
        train_end = time.time()
        print('training time: ', train_end - train_start)

        print('preparing testing data...')
        testing_data, test_targets = self.__prepare_testing_data(testing)

        test_start = time.time()
        print('testing model...')
        prediction = classifier.test_model(testing_data)
        test_end = time.time()
        print('testing time: ', test_end - test_start)

        acc = self.__calculate_accuray(prediction, test_targets)

        print('accuracy', acc)
        end = time.time()
        print('total time: ', end - start)
        return acc

    def __split_data(self):
        testing = []
        training = os.listdir(self.folder)
        training.remove("truth.txt")
        if '.DS_Store' in training:
            training.remove(".DS_Store")
        num_test = int(len(training) * 0.1)

        for i in range(num_test):
            selected = random.choice(training)
            testing.append(selected)
            training.remove(selected)

        return training, testing

    def __get_classes(self, data):
        classes = {}
        with open(self.folder + '/truth.txt', 'r') as truth_file:
            truth = truth_file.read()
            for file in data:
                truth_line = re.findall(file.split('.')[0] + '.*$', truth, re.MULTILINE)[0]
                gender = truth_line.split(':::')[1]
                classes[file] = 1.0 if gender == 'FEMALE' else 0.0
        return classes

    def __prepare_training_data(self, training):
        return self.__prepare_data(training)

    def __prepare_testing_data(self, testing):
        return self.__prepare_data(testing)

    def __prepare_data(self, data):
        processed_data = []
        target_vector = None
        training_classes = self.__get_classes(data)
        for datafile in data:
            features = self.__get_features(datafile)
            if len(features) > 0:
                processed_data.extend(features)
                if training_classes[datafile] == 1.0:
                    target = np.ones((len(features), 1))
                else:
                    target = np.zeros((len(features), 1))
                if target_vector is None:
                    target_vector = target
                else:
                    target_vector = np.concatenate((target_vector, target))
        return processed_data, target_vector

    def __get_features(self, datafile):
        with open(self.folder + '/' + datafile, 'r') as file:
            return dp.parse_file(file)

    def __calculate_accuray(self, prediction, targets):
        l = prediction.shape[0]
        hits = 0
        for i in range(0, l):
            if prediction[i] == targets[i]:
                hits += 1
        return hits / l
