import re
from types import FunctionType
from config import *
import numpy as np


def approximate_root(
        f: FunctionType,
        f_prime: FunctionType,
        x0: float,
        e: float = 1e-6) -> float:
    """implements the Newton-Raphson approximation method to find the root of a
    given equation"""

    while abs(f(x0)) > e:
        if f_prime(x0) != 0:
            x1 = x0 - (f(x0) / f_prime(x0))
            x0 = x1
        else:
            raise Exception(
                'the Newton-Raphson approximation failed because f\'(x)=0')

    return x0


def generate_iv(
        Isc_ref: float,
        Voc_ref: float,
        Iph: float,
        Io: float,
        Kv: float,
        a: float,
        T: float,
        Rs: float,
        Rsh: float) -> tuple:
    """Calculates the output current for each value in the voltage array from 0 to Voc
    by solving I = f(V) using the Newton-Raphson approximation algorithm"""

    Voc = Voc_ref + Kv*(T - T_REF)    #Open circuit voltage at T (V)

    voltage = [i for i in np.linspace(0, Voc, 2000)]
    current = []

    #Approximate I for each value of V

    for i in range(0, len(voltage)):
        f = lambda I : Iph - Io*(np.exp((voltage[i] + I*Rs)/a) - 1) - (voltage[i] + I*Rs)/Rsh - I
        f_prime = lambda I : -Io*Rs/a*np.exp((voltage[i] + I*Rs)/a) - Rs/Rsh - 1
        root = approximate_root(f, f_prime, Isc_ref)
        current.append(root)

    return voltage, current


def is_float_regex(value: str) -> bool:
    """Check if a string can be converted to a float"""
    return bool(re.match(r'^[-+]?[0-9]*\.?[0-9]+$', value))