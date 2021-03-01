import numpy as np

class Predictor():
    #.dot returns the product of two matrixes
    #.T : returns transpose of a matrix : échanger les lignes et les colonnes de même indice i 
    #np.exp exponential from Euler nb
    
    def predict_Y(X, thetas):
        z = np.dot(thetas.T, X) #soit theta.T * X 
        g = 1 / (1 + np.exp(-z))
        return g

    def predict_house(grades, thetas) :
        Ys = [] #all probabilities
        for theta in thetas:
            Y = Predictor.predict_Y(grades, theta)
            Ys.append(Y)
        maxY = max(Ys) #select highest probability
        return Ys.index(maxY) #return its index i.e index of the house


    def get_predictions(students, thetas):
        predictions = []
        for student in students:
            #grades = #get_grades
            Y = Predictor.predict_house(grades, thetas)
            predictions.append(Y)
        return predictions
