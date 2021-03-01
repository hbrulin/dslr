from sorting_hat.predictor import Predictor
import numpy as np
from utils.utils import Utils

class MultiClassifier:

    learning_rate = 0.3
    iterations = 200

    def calculate_gradiant(tmp_thetas, X, Y, m) :
        grad = 0
        for i in range(0, m):
            tmp = Predictor.predict_Y(X[i], tmp_thetas)
            grad += (tmp - Y[i]) * X[i] #not sure
        grad = (1/m) * grad #inverse
        return grad

    #gradiant descent
    def get_new_theta(tmp_thetas, X, Y, m):
        gradiant = MultiClassifier.calculate_gradiant(tmp_thetas, X, Y, m)
        theta = tmp_thetas - (MultiClassifier.learning_rate * gradiant)
        return theta

    def train(data, X, Y, m):
        def one_vs_all(house): return [1 if y == house else 0 for y in Y] #see more about this

        final_thetas = []
        X = (X - X.min()) / (X.max() - X.min())
        theta_nb = len(X[0])
        for i, house in enumerate(data.houses):
            
            tmp_thetas = np.zeros(theta_nb)
            for _ in range(MultiClassifier.iterations):
                y_ova = one_vs_all(house)
                tmp_thetas = MultiClassifier.get_new_theta(tmp_thetas, X, y_ova, m)
            final_thetas.append(tmp_thetas)
        return final_thetas