import gettext
from math import ceil
from config import *
from util import generate_iv, is_float_regex
import numpy as np
import matplotlib.pyplot as plt


#i18n localization

fr_i18n = gettext.translation('simulation_script', './locales', fallback=True, languages=[LANG])
fr_i18n.install()
_ = fr_i18n.gettext


#Module specifications
#STC = Standard Test Conditions

Isc_ref = float(input(_("Short circuit current at STC (A) = ")))

Voc_ref = float(input("\n" + _("Open circuit voltage at STC (V) = ")))

Ki = float(input("\n" + _("Temperature coefficient of Isc (%/°C) = ")))

Kv = float(input("\n" + _("Temperature coefficient of Voc (%/°C) = ")))

Tn = float(input("\nNOCT (°C) = "))

n = float(input("\n" + _("Ideality factor of the junction = ")))

Ns = float(input("\n" + _("Number of cells connected in series = ")))

match UNITS['temperature']:
    case 'celcius': 
        Ta = float(input("\n" + _("Ambiant temperature (°C) = ")))
        T = Ta
    case 'fahrenheit':
        Ta = float(input("\n" + _("Ambiant temperature (°F) = ")))
        T = (Ta - 32)*(5/9)

G = float(input("\n" + _("Solar irradiation (W/m²) = ")))

match UNITS['length']:
    case 'mm':
        length = input("\n" + _("Panel length (optional) (mm) = "))
        width = input("\n" + _("Panel width (optional) (mm) = "))
    case 'in':
        length = input("\n" + _("Panel length (optional) (in) = "))
        width = input("\n" + _("Panel width (optional) (in) = "))  

T = (Tn - 20)*G/800 + T + 273.15   #Module temperature (°C)


IV = generate_iv(Isc_ref, Voc_ref, Ki, Kv, n, Ns, T, G)
voltage = IV[0]
current = IV[1]
power = np.multiply(current, voltage)


#Simulation results

Pmax = max(power)
Vmp = voltage[list(power).index(Pmax)]
Imp = current[list(power).index(Pmax)]
fill_factor = Pmax/(current[0]*voltage[-1])

print("\n" + _("-----------------------------------RESULTS-----------------------------------") + "\n")
print(_("The maximum power yielded by the module is: {0} Watt").format(ceil((Pmax*100))/100))
print(_("The max power point is estimated at I = {0} Amps and  V = {1} Volts").format(ceil((Imp*100))/100, ceil((Vmp*100))/100))
print(_("Fill Factor = {0}").format(ceil((fill_factor*100))/100))

if is_float_regex(length) and is_float_regex(width):
    match UNITS['length']:
        case 'mm':
            A = float(length)*float(width)*1e-6
        case 'in':
            A = (float(length)*float(width))/1550        
    efficiency = (Pmax/(G*A))*100     
    print(_("Efficiency = {0} %").format(ceil((efficiency*100))/100))


#Results visualization

fig = plt.figure(num="IV/PV Plot")
fig.suptitle(_("SOLAR MODULE CHARACTERISTIC CURVES"), fontname=FONT['family'], weight=FONT['weight'], color=FONT['color'], size="18")
fig.text(
    0.015, 0.90,
    (f"Temperature: {format(Ta, ".4g")} (°C)" if UNITS['temperature'] == 'celcius' else f"Temperature: {format(Ta, ".4g")} (°F)") + f"  |  Irradiation: {format(G, ".4g")} (W/m²)",
    color=FONT['color'], fontsize=10,
)
fig.set_size_inches(9, 9)
fig.patch.set_facecolor("#ffffff")

IV = plt.subplot(211)
PV = plt.subplot(212, sharex=IV)
plt.subplots_adjust(hspace=0)

IV.spines["left"].set_color("none")
IV.spines["right"].set_color("none")
IV.spines["top"].set_color("none")
IV.tick_params(axis='y', colors=FONT['color'])

IV.plot(voltage, current, "#7a76c2", linewidth=2, label="I = f(V)")
IV.set_xlim(0)
IV.set_ylim(0, 1.12*max(current))
plt.setp(IV.get_xticklabels(), visible=False)
IV.set_ylabel(_("Current") + "\n" + _("(Amp)"), fontdict=FONT, rotation=0, loc="center", labelpad=32)
IV.legend(loc="upper right")
IV.grid(c='#ffffff')
IV.set_facecolor('#eaeaf2')

PV.spines["left"].set_color("none")
PV.spines["right"].set_color("none")
PV.spines["top"].set_color("none")
PV.spines['bottom'].set_color(FONT['color'])
PV.tick_params(axis='x', colors=FONT['color'])
PV.tick_params(axis='y', colors=FONT['color'])
PV.xaxis.label.set_color(FONT['color'])

PV.plot(voltage, power, "#f62196", linewidth=2, label="P = f(V)")
PV.plot(Vmp, Pmax, "#f6a0be", marker="o", label=_("Max power point"))    #highlight max power point
PV.set_ylim(0, 1.12*max(power))
PV.set_xlabel(_("Voltage (Volt)"), fontdict=FONT)
PV.set_ylabel(_("Power") + "\n(Watt)", fontdict=FONT, rotation=0, loc="center", labelpad=32)
PV.legend(loc="upper left")
PV.grid(c='#ffffff')
PV.set_facecolor('#eaeaf2')

plt.show()