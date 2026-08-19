import gettext
from math import ceil
from config import *
from util import generate_iv, is_float_regex
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


#i18n localization

fr_i18n = gettext.translation('simulation_script', './locales', fallback=True, languages=[LANG])
fr_i18n.install()
_ = fr_i18n.gettext


#Module specifications
#STC = Standard Test Conditions

Isc_ref = float(input(_("Short circuit current at STC (A) = ")))

Voc_ref = float(input("\n" + _("Open circuit voltage at STC (V) = ")))

Imp_ref = float(input("\n" + _("Max power current at STC (A) = ")))

Vmp_ref = float(input("\n" + _("Max power voltage at STC (V) = ")))

Ki = float(input("\n" + _("Temperature coefficient of Isc (%/°C) = ")))
Ki = (Ki*Isc_ref)/100

Kv = float(input("\n" + _("Temperature coefficient of Voc (%/°C) = ")))
Kv = (Kv*Voc_ref)/100

match UNITS['temperature']:
    case 'celcius': 
        Ta = float(input("\n" + _("Cell temperature (°C) = ")))
        T = Ta + 273.15
    case 'fahrenheit':
        Ta = float(input("\n" + _("Cell temperature (°F) = ")))
        T = (Ta - 32)*(5/9) + 273.15

G = float(input("\n" + _("Solar irradiation (W/m²) = ")))

match UNITS['length']:
    case 'mm':
        length = input("\n" + _("Panel length (optional) (mm) = "))
        width = input("\n" + _("Panel width (optional) (mm) = "))
    case 'in':
        length = input("\n" + _("Panel length (optional) (in) = "))
        width = input("\n" + _("Panel width (optional) (in) = "))  


#Extract reference params

def equations(vars):
    """Uses datasheet values to define the five equations of the De Soto model 
    and their respective variables."""
    
    Iph_ref, Io_ref, a_ref, Rs_ref, Rsh_ref = vars

    E = np.exp((Vmp_ref + Imp_ref*Rs_ref)/a_ref)    #Extracted expression for readability

    #Open circuit conditions evaluated at T_2
    Eg_2 = Eg_REF*(1 - 0.0002677*(T_2 - T_REF))
    Iph_2 = Iph_ref + Ki*(T_2 - T_REF)
    Io_2 = Io_ref*((T_2/T_REF)**3)*np.exp((Eg_REF/(K*T_REF)) - (Eg_2/(K*T_2)))
    Voc_2 = Voc_ref + Kv*(T_2 - T_REF)
    a_2 = a_ref*(T_2/T_REF)

    #De Soto equations
    eq1 = (Iph_ref - Io_ref*(np.exp((Isc_ref*Rs_ref)/a_ref) - 1) - Isc_ref*(1 + (Rs_ref/Rsh_ref)))/Isc_ref
    eq2 = (Iph_ref - Io_ref*(np.exp(Voc_ref/a_ref) - 1) - Voc_ref/Rsh_ref)/Voc_ref
    eq3 = (Iph_ref - Io_ref*(E - 1) - (Vmp_ref + Imp_ref*(Rs_ref + Rsh_ref))/Rsh_ref)/Imp_ref
    eq4 = (Imp_ref/Vmp_ref - ((Io_ref/a_ref*E + 1/Rsh_ref)/(1 + (Io_ref*Rs_ref/a_ref)*E + Rs_ref/Rsh_ref)))*(Vmp_ref/Imp_ref)
    eq5 = (Iph_2 - Io_2*(np.exp(Voc_2/a_2) - 1) - Voc_2/Rsh_ref)/Isc_ref
    
    return [eq1, eq2, eq3, eq4, eq5]

a_guess = (Vmp_ref - Voc_ref)/(np.log(1 - Imp_ref/Isc_ref))
initial_guesses = [Isc_ref, Isc_ref*(np.exp(-Voc_ref/a_guess)), a_guess, 0, np.inf] 

X = fsolve(equations, initial_guesses)


#Params translated to (T,G)

Iph = (G/G_REF)*(X[0] + Ki*(T - T_REF))
Eg = Eg_REF*(1 - 0.0002677*(T - T_REF))
Io = X[1]*((T/T_REF)**3)*np.exp((Eg_REF/(K*T_REF)) - (Eg/(K*T)))
a = X[2]*(T/T_REF)
Rs = X[3]
Rsh = X[4]*(G_REF/G)


IV = generate_iv(Isc_ref, Voc_ref, Iph, Io, Kv, a, T, Rs, Rsh)
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
PV.set_ylim(0, 1.2*max(power))
PV.set_xlabel(_("Voltage (Volt)"), fontdict=FONT)
PV.set_ylabel(_("Power") + "\n(Watt)", fontdict=FONT, rotation=0, loc="center", labelpad=32)
PV.legend(loc="upper left")
PV.grid(c='#ffffff')
PV.set_facecolor('#eaeaf2')

plt.show()