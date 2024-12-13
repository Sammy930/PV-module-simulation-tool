[![Static Badge](https://img.shields.io/badge/Lang-en-red?style=flat)](https://github.com/Sammy930/PV-module-simulation-tool/blob/main/README.md)
## Description:
Cet outil de simulation, implémenté sous forme de script Python, permet de déterminer les caractéristiques électriques de modules photovoltaïques de différentes technologies en fonction de divers facteurs environnementaux.

Le script fonctionne en calculant le courant électrique produit par la cellule solaire sur une plage de valeurs de tension, en utilisant un modèle mathématique appelé "modèle à une diode", choisi pour son équilibre entre simplicité et précision. À partir de ces résultats, le script détermine le point de puissance maximale du panneau, son facteur de forme et le rendement du module. Les données sont ensuite visualisées à travers des courbes caractéristiques I(V) et P(V).

## Contexte:
Ce travail fait partie d'un projet universitaire dont l'objectif était d'étudier le comportement des modules photovoltaïques à travers une approche combinant la simulation numérique et la validation expérimentale. Dans un premier temps, un modèle mathématique à une diode a été programmé et implémenté sous Matlab afin de simuler les caractéristiques électriques I(V) et P(V) de deux technologies de modules PV le Si-monocristallin et le Si-polycristallin et de trouver les paramètres qui caractérisent ces modules. Les simulations ont permis d'analyser l'influence de paramètres clés tels que la température et l'éclairement sur les performances de ces modules. Dans un second temps, une campagne de mesures a été réalisée en conditions extérieures réelles au niveau du laboratoire des énergies renouvelables de la faculté. Les modules mono et polycristallin ont été caractérisés électriquement, avec un suivi précis de la température et de l'éclairement. Les résultats obtenus ont montré un très bon accord entre les caractéristiques I(V) réelles mesurées et celles simulées par le programme développé.

Finalement, j'ai décidé de réécrire le script Matlab original en Python car il s'agit d'un language beaucoup plus pratique et plus accessible.

## Utilisation:
Il suffit de télécharger le code source et d'exécuter simulation_script.py

## Bibliothèques tierces utilisées pour ce projet:
  - [Numpy](https://numpy.org/) pour les calculs numériques.
  - [Matplotlib](https://matplotlib.org/) pour la visualisation des données.

## Références:
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
