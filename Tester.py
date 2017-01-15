import DatasetParser as dp
import os, random
import Classifier
import numpy as np
import re


class Tester:

    def __init__(self, folder):
        self.folder = folder

    def run_evaluation(self):
        training, testing = self.__split_data()
        training_classes = self.__get_classes(training)

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
