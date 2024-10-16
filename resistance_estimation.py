from config import VT_REF
from newton_approximation import approximate_root
from numpy import exp, inf, arange, multiply

def estimate_resistance(Voc, Isc, Iph, Imp, Vmp, Pmax, Io, Vt, Ns, n, e = 1e-6):    
    """determines the values of the series and parallel resistances by making an
    initial estimation of both values and then improving it to best fit
    over the calculated value of the maximum power"""

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