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

R0_5  = np.loadtxt(fname='R0_5.dat',  usecols=(0, 1))
ax.plot(R0_5[:, 0] , R0_5[:, 1] , color=ggplot[4], marker='+', ls=lines[4], lw=2, ms=7, mew=1.5, label=r'$R_0 = 5$')
R0_10 = np.loadtxt(fname='R0_10.dat', usecols=(0, 1))
ax.plot(R0_10[:, 0], R0_10[:, 1], color=ggplot[3], marker='+', ls=lines[3], lw=2, ms=7, mew=1.5, label=r'$R_0 = 10$')
R0_20 = np.loadtxt(fname='R0_20.dat', usecols=(0, 1))
ax.plot(R0_20[:, 0], R0_20[:, 1], color=ggplot[2], marker='+', ls=lines[2], lw=2, ms=7, mew=1.5, label=r'$R_0 = 20$')
R0_40 = np.loadtxt(fname='R0_40.dat', usecols=(0, 1))
ax.plot(R0_40[:, 0], R0_40[:, 1], color=ggplot[1], marker='+', ls=lines[1], lw=2, ms=7, mew=1.5, label=r'$R_0 = 40$')
R0_80 = np.loadtxt(fname='R0_80.dat', usecols=(0, 1))
ax.plot(R0_80[:, 0], R0_80[:, 1], color=ggplot[0], marker='+', ls=lines[0], lw=2, ms=7, mew=1.5, label=r'$R_0 = 80$')

ax.set_ylabel(r'$\mu\,\,[\mathrm{D}]$')
ax.legend(loc='upper right', ncol=1)

ax.set_xlim(0.0, 105.0)
ax.set_ylim(2.6, 4.4)
ax.set_xlabel(r'$r\,\,[\AA]$')

fig.savefig('radius.png', transparent=False, bbox_inches='tight')
