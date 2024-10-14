from types import FunctionType


def approximate_root(f, f_prime, x0, e = 1e-6):

    if not (isinstance(f, FunctionType) and isinstance(f_prime, FunctionType)):
        raise TypeError("f and df must be functions")
    
    if not (
            (isinstance(x0, int) or isinstance(x0, float)) and  
            (isinstance(e, int) or isinstance(e, float))
           ):
        raise TypeError("x0 and e must be either integers or floats")


    while abs(f(x0)) > e:
        if f_prime(x0) != 0:
            x1 = x0 - (f(x0)/f_prime(x0))
            x0 = x1
        else:
            raise Exception('the Newton-Raphson approximation failed because f\'(x)=0')

    return x0