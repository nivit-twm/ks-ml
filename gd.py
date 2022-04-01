#GRADIENT DESCENT
def gradient_descent(x, y, theta, iterations, alpha):
    """
    TODO: Implement the algorithm
    Pseudocode
    for i to iterations
        compute current cost value
        compute gradients
        update theta => thetha = thetha - alpha * gradient
    return m, c
    """
    
    m = theta[1]
    c = theta[0]

    L = alpha # The learning Rate

    n = float(len(x)) # Number of elements in X

    # Performing Gradient Descent 
    for i in range(iterations): 
        Y_pred = m*x + c  # The current predicted value of Y
        D_m = (-2/n) * sum(x * (y - Y_pred))  # Derivative wrt m
        D_c = (-2/n) * sum(y - Y_pred)  # Derivative wrt c
        m = m - L * D_m  # Update m
        c = c - L * D_c  # Update c
        
    return m, c

#Pass the relevant variables to the function and get the new values back...
m, c = gradient_descent(x, y, theta, iterations, alpha)

#Print the results...
print(m, c)
