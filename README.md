[![Static Badge](https://img.shields.io/badge/Lang-en-red?style=flat)](https://github.com/Sammy930/PV-module-simulation-tool/blob/main/README.md) [![Static Badge](https://img.shields.io/badge/Lang-fr-blue?style=flat)](https://github.com/Sammy930/PV-module-simulation-tool/blob/main/README.fr.md)
## Description:
This project consists of a simulation tool implemented as a Python script which yields the electrical characteristics of photovoltaic panels of different types depending on various environmental factors

The script works by calculating the electrical current output by the solar cell across an array of voltage values through a mathematical model known as the "One diode model" which is the most widely used due to its balance of simplicity and accuracy, from these results the script determines the panel's [maximum power point](https://en.wikipedia.org/wiki/Solar-cell_efficiency#Maximum_power_point), [fill factor](https://en.wikipedia.org/wiki/Solar-cell_efficiency#Fill_factor) and the efficiency of the module. The data is then visualized through I-V and P-V characteristic curves.

## Background:
This work was part of a university project of which the objective was to study the behavior of photovoltaic modules through an approach combining numerical simulation and experimental validation. First, a single-diode mathematical model was programmed and implemented in Matlab to simulate the electrical characteristics I(V) and P(V) of two PV module technologies - monocrystalline Si and polycrystalline Si - and to find the parameters that characterize these modules. The simulations made it possible to analyze the influence of key parameters such as temperature and illumination on the performance of these modules. In a second phase, a measurement campaign was carried out under real outdoor conditions at the faculty's renewable energy laboratory. The mono and polycrystalline modules were electrically characterized, with precise monitoring of temperature and irradiation. The results obtained have shown a pretty good agreement between the actual measured I(V)/P(V) characteristics and those simulated by the developed program.

In the end i have decided to rewrite the original Matlab script in Python as it is more accessible and overall much more practical

## Usage:
Just download the source code and run simulation_script.py

## Third party libraries used for this project:
  - [Numpy](https://numpy.org/) for numerical calculations.
  - [Matplotlib](https://matplotlib.org/) for data visualization.

## References and further reading:
[1] F. Adamo, F. Attivissimo, A. Di Nisio, A. M. L. Lanzolla, and M. Spadavecchia, “Parameters estimation for a model of photovoltaic
panels,” 19th IMEKO World Congr. 2009, vol. 4, pp. 2452–2455, 2009.<br/>
[2] (s.d.). Modeling and Simulation of photovoltaic Module using MATLAB/SIMULINK. EDP
SCIENCE.<br/>
[3] (s.d.). solar photovoltaic technology basics. Récupéré sur www.energy.gov:
https://www.energy.gov/eere/solar/solar-photovoltaic-technology-basics.<br/>
[4] M.G. Villalva, J.R. Gazoli. Comprehensive approach to modeling and simulation of
photovoltaic arrays. Power Electronics, IEEE Transactions on. 24 (2009) 1198-208.<br/>
[5] A. R. Mikezi, S. W. Luque, "Effect of NOCT on Photovoltaic Performance Under Different
Environmental Conditions", IEEE Transactions on Sustainable Energy, vol. 7, no. 3, pp.
1234-1245, 2015.<br/>
