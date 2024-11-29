from types import FunctionType


def approximate_root(f: FunctionType, f_prime: FunctionType, x0: float, e = 1e-6) -> float :
    """implements the Newton-Raphson approximation method to find the root of a
    given equation"""

    while abs(f(x0)) > e:
        if f_prime(x0) != 0:
            x1 = x0 - (f(x0)/f_prime(x0))
            x0 = x1
        else:
            raise Exception('the Newton-Raphson approximation failed because f\'(x)=0')

    return x0