from sorting_hat.predictor import Predictor

class MultiClassifier:

    learning_rate = 0.3
    iterations = 200

    def calculate_gradiant(old_theta, X, Y, m) :
        theta = 0
        for i in range(0, m):
            theta += float((Predictor.predict_Y(X[i], old_theta) - Y[i] * X**i)) #not sure
        theta = (1/m) * theta #inverse
        return theta

    #gradiant descent
    def get_new_theta(old_theta, X, Y, m):
        gradiant = calculate_gradiant(old_theta, X, Y, m)
        theta = old_theta - (learning_rate * gradiant)
        return theta

    #input data?
    def train(data, X, Y, m):
        tmp_thetas = [0.0, 0.0, 0.0, 0.0] #better way to do this!
        for i in data.houses:
            for _ in range(iterations):
                new_theta = get_new_theta(thetas[i], X, Y, M)
                tmp_thetas[i] = new_theta
        return tmp_thetas