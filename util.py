from types import FunctionType
from config import VT_REF
from numpy import exp, inf, arange, multiply


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


def estimate_resistance(Voc, Isc, Iph, Imp, Vmp, Pmax, Io, Vt, Ns, n, e = 1e-6) -> float :
    """determines the values of the series and parallel resistances by making an
    initial estimation of both values and then improving it to best fit
    over the calculated maximum power value"""

    #initial estimations
    Rs = 0
    Rp = abs((Vmp + Imp*Rs)/(Iph - Imp - Io*(exp((Vmp + Imp*Rs)/VT_REF/Ns/n) - 1)))

    err = inf

    while err > e:

        voltage = [i for i in arange(0, Voc, 0.1)]
        current = []

        for i in range(0, len(voltage)):
            f = lambda I : Iph - Io*(exp((voltage[i] + I*Rs)/Vt/Ns/n) - 1) - (voltage[i] + I*Rs)/Rp - I
            f_prime = lambda I : -Io*Rs/Vt/Ns/n*exp((voltage[i] + I*Rs)/Vt/Ns/n) - Rs/Rp - 1
            root = approximate_root(f, f_prime, Isc)
            current.append(root)
    
        power = multiply(current, voltage)
        Pmax_calculated = max(power)
        err = abs(Pmax_calculated - Pmax)
        Rp = abs((voltage[0] - voltage[1])/(current[1] - current[0]))
        Rs = (voltage[-2] - voltage[-1])/(current[-1] - current[-2])
        
    return Rp, Rs