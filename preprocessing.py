import numpy as np

from sklearn import svm


class Classifier:

    def __init__(self):
        self.svc = svm.SVC()

    def train_model(self, training_data):
        training_vector, target_vector = self.__prepare_data(training_data)
        self.svc.fit(training_vector, target_vector)

    def test_model(self, test_data):
        test_vector,_ = self.__prepare_data(test_data)

    def __prepare_data(self, data):
        dimensions = len(data), len(data[0])
        input_vector = np.zeros(dimensions)
        target_vector = np.zeros(dimensions[0], 1)

        return input_vector, target_vector
