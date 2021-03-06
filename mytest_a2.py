from a2 import *
from matplotlib import pyplot as plt
from numpy import *

def test_linear_regression():
    print(problem_3_2_5())
    print(extrapolation_3_2_5())
    print(f_and_df(100))

def my_f(t):
    u=2510
    M0=2.8E6
    mdot=13.3E3
    g=9.81

    ## YOUR CODE HERE
    v = u*log(M0/(M0-mdot*t))-g*t
    return v

#test matplotlib
def test_zeros():
    x_data = arange(-10,10,0.1)
    n = len(x_data)
    y_data = zeros(n, dtype=float_)
    for i in range (n):
        y_data[i]= my_f(x_data[i])
    plt.plot(x_data,y_data)
    #plot x-axis
    plt.plot(x_data, zeros(n), color='black')
    plt.title("f(x)")
    plt.show()
    return


#test problem_4_1_19(v1, acc)
def mytest_newton_raphson():
    tol = 10E-2
    result = problem_4_1_19(335, 10E-2)
    print (result)
    print("Result OK?: ", (result - 70.8779722) < tol)

def mytest_newton_raphson_sys():
    x_data = array([0.5, 1, 1.5])
    y_data = array([2, 2.5, 2])
    x = array([1, 2, 0.5])
    result = f_4_1_26(x_data, y_data, x)
    print(result)
    result = problem_4_1_26(x_data,y_data)
    print (result)

def mytest_dcoeff():
    x_data = array([-2.2, -0.3, 0.8, 1.9])
    y_data = array([15.180, 10.962, 1.920, -2.040])
    result = interpolant_5_1_11()
    print ("Result interpolant_5_1_11: ", result)
    result2 = d_dd_5_1_11(0)
    print("Result d_dd_5_1_11(0): ", result2)
    result3 = error_5_1_11(0)
    print("Result error_5_1_11(0): ", result3)

    return
'''
    Run test
'''
#mytest_newton_raphson_sys()
mytest_dcoeff()

