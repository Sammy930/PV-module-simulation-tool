> **This work is a part of my college graduation project, the original program was written in Matlab so i decided to rewrite it in Python**

## Introduction:
This project consists of a simulation tool implemented as a Python script which yields the electrical characteristics of photovoltaic panels of different types depending on various environmental factors

The script works by calculating the electrical current output by the solar cell across an array of voltage values through a mathematical model known as the "One diode model" which is the most widely used due to its balance of simplicity and accuracy, from these results the script determines the panel's [maximum power point](https://en.wikipedia.org/wiki/Solar-cell_efficiency#Maximum_power_point), [fill factor](https://en.wikipedia.org/wiki/Solar-cell_efficiency#Fill_factor) and the efficiency of the module. The data is then visualized through I-V and P-V characteristic curves.

## Python libraries used in this project:
  - [Numpy](https://numpy.org/) for numerical calculations.
  - [Matplotlib](https://matplotlib.org/) for plotting the results.
