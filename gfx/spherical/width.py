#!/usr/bin/env python

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np

mpl.style.use('ggplot')
# The colors are from the ggplot style, consistent with grey background
ggplot = ['#E24A33', '#348ABD', '#988ED5', '#777777', '#FBC15E', '#8EBA42', '#FFB5B8']
# List of line styles
lines = ['-', '--', ':', '-.', '-', '--', ':']
params = {'text.usetex': False,
          'mathtext.fontset': 'stixsans',
          'font.size' : 14
         }
mpl.rcParams.update(params)

fig, ax = plt.subplots(figsize=(10, 5), facecolor='w', edgecolor='k')

# Read in data
w5_c20  = np.loadtxt(fname='dipole_acetone_perpendicular_w5_c20.dat',  usecols=(0, 1))
w10_c20 = np.loadtxt(fname='dipole_acetone_perpendicular_w10_c20.dat', usecols=(1,))
w20_c20 = np.loadtxt(fname='dipole_acetone_perpendicular_w20_c20.dat', usecols=(1,))
z = w5_c20[:, 0] - 20.0

ax.plot(z, w5_c20[:, 1], color=ggplot[0], marker='+', ls=lines[0], lw=2, ms=7, mew=1.5, label=r'$w = 5$')
ax.plot(z, w10_c20[:], color=ggplot[1], marker='+', ls=lines[1], lw=2, ms=7, mew=1.5, label=r'$w = 10$')
ax.plot(z, w20_c20[:], color=ggplot[2], marker='+', ls=lines[2], lw=2, ms=7, mew=1.5, label=r'$w = 20$')
ax.set_ylabel(r'$\mu\,\,[\mathrm{D}]$')
ax.legend(loc='upper right', ncol=1)

ax.set_xlim(-10.0, 25.0)
ax.set_ylim(3.0, 4.4)
ax.set_xlabel(r'$z\,\,[\AA]$')

fig.savefig('width.png', transparent=False, bbox_inches='tight')
