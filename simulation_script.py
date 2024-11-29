from math import ceil
from config import *
from util import generate_iv
import numpy as np
import matplotlib.pyplot as plt


#Module specifications
#STC = Standard Test Conditions

Isc_ref = float(input("Short circuit current at STC (A) = "))

Voc_ref = float(input("\nOpen circuit voltage at STC (V) = "))

Ki = float(input("\nTemperature coefficient of Isc (%/°C) = "))

Kv = float(input("\nTemperature coefficient of Voc (%/°C) = "))

Tn = float(input("\nNOCT (°C) = "))

n = float(input("\nIdeality factor of the junction = "))

Ns = float(input("\nNumber of cells connected in series = "))

T = float(input("\nAmbiant temperature (°C) = ")) + 273.15

G = float(input("\nSolar irradiation (W/m²) = "))

T = (Tn - 20)*G/800 + T    #Module temperature (°C)


IV = generate_iv(Isc_ref, Voc_ref, Ki, Kv, n, Ns, T, G)
voltage = IV[0]
current = IV[1]
power = np.multiply(current, voltage)


#Simulation results

Pmax = max(power)
Vmp = voltage[list(power).index(Pmax)]
Imp = current[list(power).index(Pmax)]
fill_factor = Pmax/(current[0]*voltage[-1])

print("\n-----------------------------------RESULTS-----------------------------------\n")
print(f"The maximum power yielded by the module is: {ceil((Pmax*100))/100} Watt")
print(f"The max power point is estimated at I = {ceil((Imp*100))/100} Amps and  V = {ceil((Vmp*100))/100} Volts")
print(f"Fill Factor = {ceil((fill_factor*100))/100}")

#Results visualization

fig = plt.figure(num="IV/PV Plot")
fig.suptitle("SOLAR MODULE CHARACTERISTIC CURVES", weight="bold", color="#060621", size="14")
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
PV.legend(loc="upper left")
PV.grid()

plt.show()