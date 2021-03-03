from sorting_hat.predictor import Predictor
import numpy as np
from utils.utils import Utils

class MultiClassifier:

    learning_rate = 0.3
    iterations = 200

    def gradiant_descent(tmp_thetas, X, Y, m) :
        predictions = np.zeros(m)
        for i in range(0, m):
            predictions[i] = Predictor.predict_Y(X[i], tmp_thetas)
        gradiant = np.dot(X.T, predictions - Y)
        gradiant /= m
        gradiant *= MultiClassifier.learning_rate
        tmp_thetas -= gradiant
        return tmp_thetas


    def train(data, X, Y, m):
        def one_vs_all(house): return [1 if y == house else 0 for y in Y] #see more about this

        final_thetas = []
        theta_nb = len(X[0])
        for i, house in enumerate(data.houses):
            tmp_thetas = np.zeros(theta_nb)
            for _ in range(MultiClassifier.iterations):
                y_ova = one_vs_all(house)
                tmp_thetas = MultiClassifier.gradiant_descent(tmp_thetas, X, y_ova, m)
            final_thetas.append(tmp_thetas)
        return final_thetas