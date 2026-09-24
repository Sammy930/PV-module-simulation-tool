import tomllib
from pathlib import Path

#Locate config file
script_dir = Path(__file__).resolve().parent
config_path = script_dir / "config.toml"

#Fallback values
_defaults = ('en', 'Cell', 1.3806503e-23, 1.60217646e-19, 1000, 298.15, 348.15, 1.796e-19, 
             {"family" : 'Microsoft Sans Serif', "color" : "#000000", "weight" : 'bold', "size" : '10'},
             {"temperature" : 'C', "length" : 'mm'})

LANG = _defaults[0] #Default language

#Initialize constants
K = _defaults[2]  #Boltzmann constant (J/K)

Q = _defaults[3]  #Electron charge (C)

G_REF = _defaults[4] #Irradiation at standard test conditions (W/m²)

T_REF = _defaults[5]    #Temperature at standard test conditions (K)

T_2 = _defaults[6]    #T_REF offset by 50K to evaluate the open-circuit conditions at a different temperature (K)

#Parse config
try:
    with open(config_path, "rb") as file:
        config = tomllib.load(file)
except FileNotFoundError:
    print(
        "--------------------------------------------------" + "\n" +
        "ERROR: 'config.toml' was not found" + "\n" +
        "The program will proceed with default settings" + "\n" +
        "Press Enter to continue..." + "\n" +
        "--------------------------------------------------"
    )
    config = {}
    input()

LANG = config.get("LANG", _defaults[0])

TEMP_SETTING = config.get("TEMP_SETTING", _defaults[1])

Eg_REF = config.get("Eg_REF", _defaults[7])

FONT = config.get("FONT", _defaults[8])
FONT = FONT if set(FONT.keys()) == set(_defaults[8].keys()) else _defaults[8]

UNITS = config.get("UNITS", _defaults[9])
UNITS  = UNITS  if set(UNITS.keys())  == set(_defaults[9].keys())  else _defaults[9]