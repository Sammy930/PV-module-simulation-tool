from types import FunctionType
from config import Q, K, G_REF, T_REF
from numpy import exp, inf, arange


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


def generate_iv(Imp_ref, Vmp_ref, Isc_ref, Voc_ref, Ki, Kv, n, Ns, T, G) -> tuple:
    
    Pmax_ref = Imp_ref * Vmp_ref    #Maximum power at STC (W)

    Vt = (K*T)/Q    #Thermal voltage at T (V)

    Iph = Isc_ref*(G/G_REF) + Ki*(T - T_REF)    #Photocurrent (A)

    Voc = Voc_ref + Kv*(T - T_REF)    #Open circuit voltage at T (V)

    Io = Isc_ref/(exp(Voc/(n*Ns*Vt)) - 1)    #Saturation current at T (A)

    Rp, Rs = inf, 0    #Series and shunt resistance


    voltage = [i for i in arange(0, Voc + 1, 0.1)]
    current = []


    #Approximate I for each value of V

    for i in range(0, len(voltage)):
        f = lambda I : Iph - Io*(exp((voltage[i] + I*Rs)/Vt/Ns/n) - 1) - (voltage[i] + I*Rs)/Rp - I
        f_prime = lambda I : -Io*Rs/Vt/Ns/n*exp((voltage[i] + I*Rs)/Vt/Ns/n) - Rs/Rp - 1
        root = approximate_root(f, f_prime, Isc_ref)
        current.append(root)

    return voltage, current