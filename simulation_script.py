from math import ceil
from config import *
from util import approximate_root, estimate_resistance
from numpy import exp, arange, multiply, inf
import matplotlib.pyplot as plt


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

Vt = (K*T)/Q    #Thermal voltage at T (V)

Iph = Isc_ref*(G/G_REF) + Ki*(T - T_REF)    #Photocurrent (A)

Voc = Voc_ref + Kv*(T - T_REF)    #Open circuit voltage at T (V)

Io = Isc_ref/(exp(Voc/(n*Ns*Vt)) - 1)    #Saturation current at T (A)

R = estimate_resistance(Voc, Isc_ref, Iph, Imp_ref, Vmp_ref, Io, Vt, Ns, n)
Rp, Rs = R[0], R[1]    #Series and shunt resistances


voltage = [i for i in arange(0, Voc, 0.1)]    
current = []


#Approximate I for each value of V

for i in range(0, len(voltage)):
    f = lambda I : Iph - Io*(exp((voltage[i] + I*Rs)/Vt/Ns/n) - 1) - (voltage[i] + I*Rs)/Rp - I
    f_prime = lambda I : -Io*Rs/Vt/Ns/n*exp((voltage[i] + I*Rs)/Vt/Ns/n) - Rs/Rp - 1
    root = approximate_root(f, f_prime, Isc_ref)
    current.append(root)


#Simulation results

power = multiply(current, voltage)
Pmax = max(power)
Vmp = voltage[list(power).index(Pmax)]
Imp = current[list(power).index(Pmax)]
fill_factor = Pmax/(current[0]*voltage[-1])
R = estimate_resistance(Voc, Isc_ref, Iph, Imp_ref, Vmp_ref, Io, Vt, Ns, n)

print("\n-----------------------------------RESULTS-----------------------------------\n")
print(f"The maximum power yielded by the module is: {ceil((Pmax*100))/100} Watt")
print(f"The max power point is estimated at I = {ceil((Imp*100))/100} Amps and  V = {ceil((Vmp*100))/100} Volts")
print(f"Fill Factor = {ceil((fill_factor*100))/100}")
print(f"Approximated resistance values:   Rs = {ceil(R[1]*100)/100} Ω    Rp = {ceil(R[0]*100)/100} Ω")

#Results visualization

fig = plt.figure()
fig.suptitle("SOLAR PANEL CHARACTERISTIC CURVES", weight="bold", color="#060621", size="14")
fig.set_size_inches(8, 6.75)
fig.patch.set_facecolor("#cacfe6")

IV = plt.subplot(211)
PV = plt.subplot(212, sharex=IV)
plt.subplots_adjust(hspace=0)

IV.plot(voltage, current, "b", linewidth=2, label="I = f(V)")
IV.set_xlim(0)
IV.set_ylim(0, 1.12*max(current))
plt.setp(IV.get_xticklabels(), visible=False)
IV.set_ylabel("Current\n(Amp)", fontdict=FONT, rotation=0, loc="center", labelpad=32)
IV.legend(loc="upper right")
IV.grid()

PV.plot(voltage, power, "r", linewidth=2, label="P = f(V)")
PV.plot(Vmp, Pmax, "b", marker="o", label="Max power point")    #highlight max power point
PV.set_ylim(0, 1.12*max(power))
PV.set_xlabel("Voltage (Volt)", fontdict=FONT)
PV.set_ylabel("Power\n(Watt)", fontdict=FONT, rotation=0, loc="center", labelpad=20)
PV.legend(loc="upper center")
PV.grid()

plt.show()