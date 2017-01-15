import numpy as np

from sklearn import svm


class Classifier:

    def __init__(self):
        self.svc = None

    def train_model(self, training_data, target_vector):
        self.svc = svm.SVC()
        training_vector = self.__prepare_data(training_data)
        self.svc.fit(training_vector, target_vector.ravel())

    def test_model(self, test_data):
        test_vector = self.__prepare_data(test_data)
        return self.svc.predict(test_vector)

    def __prepare_data(self, data):
        dimensions = (len(data), len(data[0]))
        input_vector = np.zeros(dimensions)

        i = 0
        for instance in data:
            j = 0
            for _, feature in instance.items():
                input_vector[i][j] = feature
                j += 1
            i += 1
        return input_vector
