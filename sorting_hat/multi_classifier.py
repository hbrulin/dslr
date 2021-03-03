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

    #so that I know if my predictions concern the house on which I want the theta
    def one_vs_all(Y, house):
        y_ova = []
        for y in Y:
            if y == house:
                y_ova.append(1)
            else: 
                y_ova.append(0)
        return y_ova

    def train(data, X, Y, m):
        final_thetas = []
        theta_nb = len(X[0])
        for i, house in enumerate(data.houses):
            y_ova = MultiClassifier.one_vs_all(Y, i)
            tmp_thetas = np.zeros(theta_nb)
            for _ in range(MultiClassifier.iterations):
                tmp_thetas = MultiClassifier.gradiant_descent(tmp_thetas, X, y_ova, m)
            final_thetas.append(tmp_thetas)
        return final_thetas