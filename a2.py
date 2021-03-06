#!/usr/bin/env python

from numpy import array, arange, mean, sum, log, zeros,sqrt,prod, diagonal,shape, float_, dot, argmax

'''
NOTE: You are not allowed to import any function from numpy's linear 
algebra library, or from any other library except math.
'''

'''
    Part 1: Warm-up (bonus point)
'''

def spaces_and_tabs():
    '''
    A few of you lost all their marks in A1 because their file 
    contained syntax errors such as:
      + Missing ':' at the end of 'if' or 'for' statements.
      + A mix of tabs and spaces to indent code. Remember that indendation is part
        of Python's syntax. Mixing tabs and spaces is not good because it
        makes indentation levels ambiguous. For this reason, files 
        containing a mix of tabs and spaces are invalid in Python 3. This
        file uses *spaces* for indentation: don't add tabs to it!
    Remember that you are strongly encouraged to check the outcome of the tests
    by running pytest on your computer and by checking Travis.
    Task: Nothing to implement in this function, that's a bonus point, yay!
          Just don't loose it by adding syntax errors to this file...
    Test: 'tests/test_spaces_and_tabs.py'
    '''
    return ("I won't use tabs in my code",
            "I will make sure that my code has no syntax error",
            "I will check the outcome of the tests using pytest or Travis"
            )

'''
    Part 2: Linear regression
'''

def problem_3_2_5():
    '''
    We will solve problem 3.2.5 in the textbook.
    Arrays 'year' and 'ppm' contain the annual atmospheric CO2 concentration
    in parts per million in Antarctica.
    Task: This function must return the average increase in ppm per year,
          obtained by fitting a straight line to the data.
    Test: Function 'test_problem' in 'tests/test_problem_3_2_5.py'
    Hint: Fitting is meant in the least-square sense.
    '''

    year = arange(1994, 2010)  # from 1994 to 2009
    ppm = array([356.8, 358.2, 360.3, 361.8, 364.0, 365.7, 366.7, 368.2,
                 370.5, 372.2, 374.9, 376.7, 378.7, 381.0, 382.9, 384.7])

    ## YOUR CODE HERE
    a, b = linear_regression(year, ppm)
    return b
    raise Exception("Not implemented")

def extrapolation_3_2_5():
    '''
    Task: Return the estimated atmospheric CO2 concentration in Antarctica 
          in 2020.
    Test: Function 'test_2020' in 'tests/test_problem_3_2_5.py'
    Hint: Use the result of the previous function.
    '''
    ## YOUR CODE HERE
    year = arange(1994, 2010)  # from 1994 to 2009
    ppm = array([356.8, 358.2, 360.3, 361.8, 364.0, 365.7, 366.7, 368.2,
                 370.5, 372.2, 374.9, 376.7, 378.7, 381.0, 382.9, 384.7])
    a, b = linear_regression(year, ppm)
    return a + b*2020
    raise Exception("Not implemented")

'''
    Added functions
'''
#From course notes
def linear_regression(x_data, y_data):
    '''
    Returns (a, b, stdev)
    '''
    xbar = mean(x_data)
    ybar = mean(y_data)
    b = sum(y_data*(x_data-xbar))/sum(x_data*(x_data-xbar))
    a = ybar - xbar*b
    return (a, b)

'''
    Part 3: Non-linear equations
'''

'''
    We will solve problem 4.1.19 in the textbook:
    "
        The speed v of a Saturn V rocket in vertical flight near the surface
        of earth can be approximated by:
            v = u*log(M0/(M0-mdot*t))-g*t
            (log base is e)
        where:
           * u = 2510 m /s is the velocity of exhaust relative to the rocket
           * M0 = 2.8E6 kg is the mass of the rocket at liftoff
           * mdot = 13.3E3 kg/s is the rate of fuel consumption
           * g = 9.81 m/s**2 is the gravitational acceleration
           * t is the time measured from liftoff
    "
'''

def f_and_df(t):
    '''
    Task: return a tuple containing (1) the value of the velocity v
          at time t, (2) the value of the derivative of v at time t.
    Parameter: 't' is the value at which the function and its derivative
               must be evaluated.
    Example: f_and_df(100) must be close to (636.3361111401882, 12.89952381017656)
    Test: function 'f_and_df' in 'tests/test_problem_4_1_19'
    Hint: to compute f', use the central approximation
    '''

    u=2510
    M0=2.8E6
    mdot=13.3E3
    g=9.81

    ## YOUR CODE HERE
    v = u*log(M0/(M0-mdot*t))-g*t
    df = u*mdot/(M0-mdot*t)-g
    return v, df
    raise Exception("Not implemented")

def problem_4_1_19(v1, acc):
    '''
    Task: return the time in seconds when the rocket reaches velocity v1,
          with accuracy acc.
    Parameters:  'v1' is a float representing the velocity of the rocket in m/s.
                 'acc' is a float representing the accuracy of the solution.
    Example: problem_4_1_19(335, 0.1) = 70.877972
    Test: function 'test_problem' in 'tests/test_problem_4_1_9.py'
    Hint: plot the function to get a first guess at the solution.
    '''

    #initial estimate is x = v1/2
    return newton_raphson(saturn_rocket_speed,v1,saturn_speed_diff,v1/2,acc)
    raise Exception("Not implemented")   

'''
    Added functions
'''
#From course notes, slightly modifed
#@adj is adjustment to f to solve root of equation f(x) = f - adj
def newton_raphson(f, adj, diff, init_x, tol, max_iter=1000):
    '''
    f is the function for which a zero is sought
    diff is the derivative of the function
    init_x is the initial estimate
    tol is the tolerance (accuracy) of the solution
    max_iter is the desired maximal number of iterations
    '''
    x = init_x
    for i in range(max_iter): # we will break out of the loop when we find the root
        delta_x = -(f(x)-adj)/diff(x)
        x = x + delta_x
        if abs(delta_x) <= tol: # check delta_x we just used to move x
            return x
    raise Exception("Unable to find a root")

def saturn_rocket_speed(t):
    u=2510
    M0=2.8E6
    mdot=13.3E3
    g=9.81

    v = u*log(M0/(M0-mdot*t))-g*t
    return v

def saturn_speed_diff(t):
    u=2510
    M0=2.8E6
    mdot=13.3E3
    g=9.81

    df = u * mdot / (M0 - mdot * t) - g
    return df


'''
    Part 4: Systems of non-linear equations
'''

'''
    We will solve problem 4.1.26 from the textbook:
        "
        The equation of a circle is: (x-a)**2 + (y-b)**2 = R**2
        where R is the radius and (a,b) are the coordinates of the center.
        Given the coordinates of three points p1, p2 and p3, find a, b
        and R such that the circle of center (a, b) and radius R passes
        by p1, p2 and p3.
        "
'''

def f_4_1_26(x_data, y_data, x):
    '''
    The problem consists in finding the zero of a
    function of 3 variables (a, b and R). 
    Task: return an array containing the coordinates of f(x) such
          that the problem can be solved by finding a zero of f. 
          x is a vector representing (a, b, R).
    Parameters: + 'x_data' is an array of 3 coordinates representing the abscissa
                   of the input points.
                + 'y_data' is an array of 3 coordinates representing the ordinates
                   of the input points.
                + 'x' is an array of 3 coordinates representing (a, b, R)
    Example: f_4_1_26(array([0.5, 1, 1.5]),
                      array([2, 2.5, 2]),
                      array([1, 2, 0.5])) = [0, 0, 0]
    Test: function 'test_f' in 'tests/test_problem_4_1_26.py'
    '''
    ## YOUR CODE HERE
    f = array([
        (x_data[0] - x[0])**2 + (y_data[0] - x[1])**2 - x[2]**2,
        (x_data[1] - x[0])**2 + (y_data[1] - x[1])**2 - x[2]**2,
        (x_data[2] - x[0])**2 + (y_data[2] - x[1])**2 - x[2]**2
        ])
    return f
    raise Exception("Not implemented")

def problem_4_1_26(x_data, y_data):
    '''
    Task: return a, b and R so that the circle of center (a, b) and radius
          R passes by the 3 points defined by x_data and y_data.
    Parameters: + 'x_data' is an array of 3 coordinates representing the abscissa
                   of the input points.
                + 'y_data' is an array of 3 coordinates representing the ordinates
                   of the input points.
    Example: problem_4_1_26(array([0.5, 1, 1.5]), array([2, 2.5, 2]))
             must return [1., 2., 0.5]
    Test: function 'test_problem' in 'tests/test_problem_4_1_26.py''
    Hint: use Newton-Raphson for systems of non-linear equations to find
          a zero of f_4_1_26.
    '''
    ## YOUR CODE HERE
    a = mean(x_data)
    b = mean(y_data)
    rs = []
    #Get a good estimate of x
    #Taken from https://waxworksmath.com/Authors/G_M/Kiusalaas/NMIEW_Python/kiusalaas.html
    for x,y in zip(x_data, y_data):
        rs.append(sqrt((x-a)**2 + (y-b)**2))
    r = mean(rs)
    return newton_raphson_system(f_4_1_26,x_data, y_data,array([a,b,r]))
    raise Exception("Not implemented")

'''
    Added functions
'''

#From notes, slightly modified
def newton_raphson_system(f, x_data, y_data, init_x, epsilon=10E-4, max_iterations=100):
    '''
    Return a solution of f(x)=0 by Newton-Raphson method.
    init_x is the initial guess of the solution
    '''
    x = init_x
    for i in range(max_iterations):
        J = jacobian(f, x_data, y_data, x)
        delta_x = gauss_multiple_pivot(J, -f(x_data, y_data, x)) # uses function from A1
        x = x + delta_x
        if sqrt(sum(delta_x**2)) <= epsilon:
            print("Converged in {} iterations".format(i))
            return x
    raise Exception("Could not find root!")

#From notes
def jacobian(f, x_data, y_data, x):
    '''
    Returns the Jacobian matrix of f taken in x J(x)
    '''
    n = len(x)
    jac = zeros((n, n))
    h = 10E-4
    fx = f(x_data, y_data,x)
    # go through the columns of J
    for j in range(n):
        # compute x + h ej
        old_xj = x[j]
        x[j] += h
        # update the Jacobian matrix (eq 3)
        # Now x is x + h*ej
        jac[:, j] = (f(x_data, y_data, x)-fx) / h
        # restore x[j]
        x[j] = old_xj
    return jac

'''
    Part 5: Interpolation and Numerical differentiation
'''

'''
    We will solve problem 5.1.11 from the textbook:
        " 1. Use polynomial interpolation to compute f' and f'' at x using
          the data in x_data and y_data:
                x_data = array([-2.2, -0.3, 0.8, 1.9])
                y_data = array([15.180, 10.962, 1.920, -2.040])
          2. Given that f(x) = x**3 - 0.3*x**2 -
             8.56*x + 8.448, gauge the accuracy of the result."
'''

def interpolant_5_1_11():
    '''
    Task: return an array containing the coefficients of the polynomial
          of degree 3 interpolating the data points.
    Test: function 'test_interpolant' of 'tests/test_problem_5_1_11.py'
    Hint: use code from Chapters 2 and 3.
    '''
    ## YOUR CODE HERE
    x_data = array([-2.2, -0.3, 0.8, 1.9])
    y_data = array([15.180, 10.962, 1.920, -2.040])
    m=3 #desired degree of interpolation polynomial
    return polynomial_fit(x_data, y_data, m)
    raise Exception("Not implemented")

def d_dd_5_1_11(x):
    '''
    Task: return a tuple containing the value of f' and f'' at x.
    Parameter: x is the value at which f' and f'' must be computed.
    Test: function 'test_d_dd' of 'tests/test_problem_5_1_11.py'
    Example: d_dd_5_1_11(0) must return (8.56, -0.6).
    Hint: differentiate the interpolant returned by the previous function.
    '''
    ## YOUR CODE HERE
    x_data = array([-2.2, -0.3, 0.8, 1.9])
    y_data = array([15.180, 10.962, 1.920, -2.040])
    m = len(x_data) -1
    coeffs = polynomial_fit(x_data, y_data, m)
    d_coeffs = df_interpol(coeffs, m)
    dd_coeffs = df_interpol(d_coeffs,m-1)   #d_coeffs has m-1 coefficients
    df = eval_p(d_coeffs,x)
    ddf = eval_p(dd_coeffs,x)
    return df,ddf
    raise Exception("Not implemented")

def error_5_1_11(x):
    '''
    Task: return a tuple containing the errors made by your previous
           approximation of f' and f'' at x.
    Parameter:  x is the value at which f' and f'' must be computed.
    Test: function 'test_error' of  'tests/test_problem_5_1_11.py'
    Example: error(0) must return
    Hint: differentiate x**3 - 0.3*x**2 - 8.56*x + 8.448 manually and compare
          the result to the output of the previous function.
    '''
    ## YOUR CODE HERE
    df = 2*(x**2)-0.6*x-8.56
    ddf = 4*x-0.6
    a, b = d_dd_5_1_11(x)
    return df - a, ddf - b   #return error
    raise Exception("Not implemented")

'''
    Added functions
'''
#From course notes, slightly modified
def df_interpol(coeffs, n):
    d_coeffs = zeros(n)
    for i in range(n):
        d_coeffs[i] = (i+1)*coeffs[i+1] # differentiation from coefficients
    return d_coeffs

#From course notes, CHAPTER 3, slightly modified
def polynomial_fit(x_data, y_data, m):
    '''
    Returns the ai
    '''
    # x_power[i] will contain sum_i x_i^k, k = 0, 2m
    x_powers = zeros(2*m+1, dtype=float_)
    b = zeros(m+1, dtype = float_)
    for i in range(2*m+1):
        x_powers[i] = sum(x_data**i)
        if i < (m+1):
            b[i] = sum(y_data*x_data**i)
    a = zeros((m+1, m+1), dtype = float_)
    for k in range(0,m+1):
        for j in range(0,m+1):
            a[k, j] = x_powers[j+k]
    return gauss_multiple_pivot(a,b)

#From course notes, CHAPTER 4
def eval_p(a, x):
    '''
    Returns P(x) where the coefficients of P are in a
    '''
    n = len(a)
    p = a[n-1]
    for i in range(2, n+1):
        p = a[n-i] + x*p
    return p

'''
    From A1
'''

def gauss_multiple_pivot(a, b):
    '''
      Task: This function returns the same result as the previous one,
            except that it uses scaled row pivoting.
      Parameters: a is a numpy array representing a square matrix. b is a numpy
            array representing a matrix with as many lines as in a.
      Test: This function is is tested by the function
            test_gauss_multiple_pivot in tests/test_gauss_multiple.py.
    '''

    ## YOUR CODE GOES HERE
    gauss_elimin_pivot(a,b)
    ''' The determinant of a triangular matrix 
        is the product of the diagonal elements
    '''
    det = prod(diagonal(a))
    assert(det!=0)
    return gauss_substitution(a,b)
    raise Exception("Function not implemented")



#for gauss_multiple_pivot
def gauss_elimin_pivot(a,b,verbose=False):
    #A
    n, m = shape(a)     #must be square
    #B
    n2=1
    m2=1
    if len(shape(b))==1:
        n2, = shape(b)   #does not need to be square
    elif len(shape(b))==2:
        n2, m2 = shape(b)   #does not need to be square
    else:
        raise Exception("B has more than 2 dimensions.")
    assert(n==n2)
    #Used for pivoting
    s = zeros(n, dtype =float_)
    for i in range (0,n):
        s[i] = max(abs(a[i, :])) #max of row i in A
    # Pivoting
    #print(a)
    for k in range (0,n-1):     #range(start,stop[,step])
        p = argmax(abs(a[k:, k]) / s[k:]) + k
        swap(a,p,k) #swap rows in matrix A
        swap(b,p,k) #swap rows in matrix b
        swap(s,p,k) #swap rows in vector  s
        #Apply row operations
        for i in range (k+1, n):
            assert(a[k,k]!=0) #verify what to do later
            if(a[i,k]!=0): #no need to do anything when lambda is 0
                lmbda = a[i,k]/a[k,k]
                a[i,k:n]=a[i,k:n] - lmbda * a[k,k:n] #apply operation to row i of A
                if m2==1:
                    b[i] = b[i] - lmbda * b[k]  # apply operation to row i of b
                else:
                    b[i,:]=b[i,:] - lmbda * b[k,:] #apply operation to row i of b
            if verbose:
                print('a:\n', a, '\nb:\n', b, '\n')


def gauss_substitution(a, b):
    n, m = shape(a)
    # Verify the n*n dimensions of B
    n2 = 1
    m2 = 1
    if len(shape(b)) == 1:
        n2, = shape(b)
    elif len(shape(b)) == 2:
        n2, m2 = shape(b)
    else:
        raise Exception("B has more than 2 dimensions")
    assert (n == n2)
    if m2 > 1:
        x = zeros([n, m2], dtype=float_)
        for i in range(n - 1, -1,
                       -1):  # decreasing index, #range(start,stop[,step]) -> iterates over every row of solution matrix x
            for j in range(0, m2):
                x[i, j] = (b[i, j] - dot(a[i, i + 1:], x[i + 1:, j])) / a[i, i]
        # return n*m system of solutions
        return x
    else:
        x = zeros([n], dtype=float_)
        for i in range(n - 1, -1,
                       -1):  # decreasing index, #range(start,stop[,step]) -> iterates over every row of solution matrix x
            x[i] = (b[i] - dot(a[i, i + 1:], x[i + 1:])) / a[i, i]
        # return n*m system of solutions
        return x

    # for gauss_multiple_pivot


def swap(a, i, j):
    if len(shape(a)) == 1:
        a[i], a[j] = a[j], a[i]  # unpacking
    else:
        a[[i, j], :] = a[[j, i], :]