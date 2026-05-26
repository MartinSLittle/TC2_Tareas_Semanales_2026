#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:46:47 2026

@author: martin
"""

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from scipy import signal as sig

# Librería de la cátedra (UTN/UBA)
from pytc2.sistemas_lineales import analyze_sys

# Configuración de estilo (la mantenemos igual)
fig_sz_x = 13
fig_sz_y = 7
fig_dpi = 80 
fig_font_size = 13
mpl.rcParams['figure.figsize'] = (fig_sz_x, fig_sz_y)
mpl.rcParams['figure.dpi'] = fig_dpi
plt.rcParams.update({'font.size':fig_font_size})

# --- COMIENZO DE LA SIMULACIÓN NORMALIZADA ---

orden = 6
# Frecuencia angular normalizada
w0 = 1.0 

# Coeficientes para H(s) = (1*s - 1) / (1*s + 1)
# El primer valor es el coeficiente de 's', el segundo es el término independiente.
num, den = sig.butter(orden, w0, btype='low', analog=True, output='ba')
H_butter = sig.TransferFunction(num, den)

# analyze_sys hace todo: diagrama de Bode (módulo y fase), polos y ceros y respuesta al impulso.
analyze_sys(H_butter, sys_name='Pasa-bajos Butterworth 6to Orden')