import numpy as np
def perceptron_train(X, Y):
    w = np.zeros_like(np.arange(np.size(X, 1), dtype=float)) # Initialize weights
    b = 0 # Initialize bias
    update = 1 # Tracks if weights/bias have been updated during epoch
    
    while update == 1:
        update = 0
        for index in range(0, np.size(X, axis=0)):
            a = calc_activation(w, X[index], b) # calculate activation
            if Y[index]*a <= 0:
                for i in range(0, np.size(w)): # update weights
                    w[i] += Y[index]*X[index][i]
                b += Y[index] # update bias
                update = 1
    return w, b
        
def calc_activation(W, X, B):
    if (np.size(X) != np.size(W)):
        print("Incorrect dimensions")
        return
    a = 0
    for index in range(0, np.size(X)):
        a += W[index]*X[index]
    return a + B

def perceptron_test(X_test, Y_test, w, b):
    acc = 0.0
    for index in range(0, np.size(X_test, 0)):
        a = calc_activation(w, X_test[index], b)
        if Y_test[index]*a > 0:
            acc += 1
    return acc/np.size(X_test, 0)
