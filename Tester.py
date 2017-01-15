import DatasetParser as dp
import os, random
import Classifier
import numpy as np
import re


class Tester:

    def __init__(self, folder):
        self.folder = folder

    def run_evaluation(self):
        print('Evaluation start')
        training, testing = self.__split_data()
        print('preparing data...')
        training_data, target_vector = self.__prepare_training_data(training)
        classifier = Classifier.Classifier()
        print('training model...')
        classifier.train_model(training_data, target_vector)

    def __split_data(self):
        testing = []
        training = os.listdir(self.folder)
        training.remove("truth.txt")
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
        training_data = []
        target_vector = None
        training_classes = self.__get_classes(training)
        for datafile in training:
            features = self.__get_features(datafile)
            if len(features) > 0:
                training_data.extend(features)
                if training_classes[datafile] == 1.0:
                    target = np.ones((len(features), 1))
                else:
                    target = np.zeros((len(features), 1))
                if target_vector is None:
                    target_vector = target
                else:
                    target_vector = np.concatenate((target_vector, target))
        return training_data, target_vector

    def __prepare_testing_data(self, testing):
        pass

    def __get_features(self, datafile):
        with open(self.folder + '/' + datafile, 'r') as file:
            return dp.parse_file(file)
