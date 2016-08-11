#!/usr/bin/env python

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np

mpl.style.use('ggplot')
# The colors are from the ggplot style, consistent with grey background
ggplot = ['#E24A33', '#348ABD', '#988ED5', '#777777', '#FBC15E', '#8EBA42', '#FFB5B8']
# List of line styles
lines = ['-', '--', ':', '-.', '-', '--', ':']
# List of labels
labs = [r'$R_0 = 40$', r'$R_0 = 20$', r'$R_0 = 10$', r'$R_0 = 5$']
params = {'text.usetex': False,
          'mathtext.fontset': 'stixsans',
          'font.size' : 14
         }
mpl.rcParams.update(params)

fig, ax = plt.subplots(figsize=(10, 5), facecolor='w', edgecolor='k')

fname='curv_dip_acetone_perpen.dat'

# Read columns
data = np.loadtxt(fname, usecols=(0, 1, 2, 3, 4))
for col in range(1, 5):
    ax.plot(data[:, 0], data[:, col], color=ggplot[col-1], marker='+', ls=lines[col-1], lw=2, ms=7, mew=1.5, label=labs[col-1])
    ax.set_ylabel(r'$\mu\,\,[\mathrm{D}]$')
    ax.legend(loc='upper right', ncol=1)

ax.set_xlim(-5.0, 10.0)
ax.set_ylim(0.0, 1.4)
ax.set_xlabel(r'$z\,\,[\AA]$')

fig.savefig('curvature.png', transparent=False, bbox_inches='tight')
