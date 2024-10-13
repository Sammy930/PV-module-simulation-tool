from config import *
from numpy import exp


#Panel specifications
#STC = Standard Test Conditions

Isc_ref = float(input("Short circuit current at STC (A) = "))

Voc_ref = float(input("Open circuit voltage at STC (V) = "))

Imp_ref = float(input("Maximum power current at STC (A) = "))

Vmp_ref = float(input("Maximum power voltage at STC (V) = "))

Ki = float(input("Temperature coefficient of the current = "))

Kv = float(input("Temperature coefficient of the voltage = "))

n = float(input("Ideality factor of the junction = "))

Ns = float(input("Number of cells connected in series = "))

T = float(input("Panel temperature (°C) = ")) + 273.15

G = float(input("Solar irradiation (W/m²) = "))