from sorting_hat.predictor import Predictor

class MultiClassifier:

    learning_rate = 0.3
    iterations = 200

    def calculate_gradiant(old_theta, X, Y, m) :
        theta = 0
        for i in range(0, m):
            theta += float((Predictor.predict_Y(X[i], old_theta) - Y[i]) * X**i) #not sure
        theta = (1/m) * theta #inverse
        return theta

    #gradiant descent
    def get_new_theta(old_theta, X, Y, m):
        gradiant = MultiClassifier.calculate_gradiant(old_theta, X, Y, m)
        theta = old_theta - (MultiClassifier.learning_rate * gradiant)
        return theta

    def train(data, X, Y, m):
        tmp_thetas = [0.0, 0.0, 0.0, 0.0] #better way to do this!
        for i, house in enumerate(data.houses):
            for _ in range(MultiClassifier.iterations):
                new_theta = MultiClassifier.get_new_theta(tmp_thetas[i], X, Y, m)
                tmp_thetas[i] = new_theta
        return tmp_thetas