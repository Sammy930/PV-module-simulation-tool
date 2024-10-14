from config import *
from numpy import exp, arange


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


Pmax_ref = Imp_ref * Vmp_ref    #Maximum power at STC (W)

Vt = (K*T)/Q  #Thermal voltage at T (V)

Ipv = (Isc_ref + (Ki/100)*Isc_ref*(T - T_REF))*(G/G_REF)    #Photocurrent (A)

Isc = Isc_ref + (Ki/100)*Isc_ref*(T - T_REF)    #Short circuit current at T (A)

Voc = Voc_ref + (Kv/100)*Voc_ref*(T - T_REF)    #Open circuit voltage at T (V)

Io_ref = Isc_ref/(exp(Voc_ref/(n*Ns*VT_REF)) - 1)   #Saturation current at STC (A)

Io = Isc/(exp(Voc/(n*Ns*Vt)) - 1)   #Saturation current at T (A)


voltage = [i for i in arange(0, Voc, 0.1)]    
current = []
power = []