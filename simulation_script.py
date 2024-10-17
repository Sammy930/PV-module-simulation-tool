from config import *
from newton_approximation import approximate_root
from resistance_estimation import estimate_resistance
from numpy import exp, arange, multiply
import matplotlib.pyplot as plt


#Panel specifications
#STC = Standard Test Conditions

Isc_ref = 5.95

Voc_ref = 22.4

Imp_ref = 5.62

Vmp_ref = 17.8

Ki = 0.06

Kv = -0.35

n = 1

Ns = 36

T = 25 + 273.15

G = 1000


Pmax_ref = Imp_ref * Vmp_ref    #Maximum power at STC (W)

Vt = (K*T)/Q  #Thermal voltage at T (V)

Iph = (Isc_ref + (Ki/100)*Isc_ref*(T - T_REF))*(G/G_REF)    #Photocurrent (A)

Isc = Isc_ref + (Ki/100)*Isc_ref*(T - T_REF)    #Short circuit current at T (A)

Voc = Voc_ref + (Kv/100)*Voc_ref*(T - T_REF)    #Open circuit voltage at T (V)

Io_ref = Isc_ref/(exp(Voc_ref/(n*Ns*VT_REF)) - 1)   #Saturation current at STC (A)

Io = Isc/(exp(Voc/(n*Ns*Vt)) - 1)   #Saturation current at T (A)

R = estimate_resistance(Voc, Isc, Iph, Imp_ref, Vmp_ref, Pmax_ref, Io, Vt, Ns, n)
Rp, Rs = R[0], R[1]

voltage = [i for i in arange(0, Voc, 0.1)]    
current = []


for i in range(0, len(voltage)):
    f = lambda I : Iph - Io*(exp((voltage[i] + I*Rs)/Vt/Ns/n) - 1) - (voltage[i] + I*Rs)/Rp - I
    f_prime = lambda I : -Io*Rs/Vt/Ns/n*exp((voltage[i] + I*Rs)/Vt/Ns/n) - Rs/Rp - 1
    root = approximate_root(f, f_prime, Isc)
    current.append(root)

power = multiply(current, voltage)


#Results visualization

fig = plt.figure()
fig.suptitle("Solar panel characteristic curves")
fig.set_size_inches(8, 6.75)

IV = plt.subplot(211)
IV.plot(voltage, current, "b", label="I = f(V)")
IV.set_xlim(0)
IV.set_ylim(0, 1.12*max(current))
plt.setp(IV.get_xticklabels(), visible=False)
IV.set_ylabel("Current\n(Amp)",rotation=0, loc="center", labelpad=32)
IV.legend()
IV.grid()

PV = plt.subplot(212, sharex=IV)
PV.plot(voltage, power, "r", label="P = f(V)")
PV.set_ylim(0, 1.12*max(power))
PV.set_xlabel("Voltage (Volt)")
PV.set_ylabel("Power\n(Watt)",rotation=0, loc="center", labelpad=20)
PV.legend(loc="upper center")
PV.grid()

plt.subplots_adjust(hspace=0)
plt.show()