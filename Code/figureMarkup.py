
import matplotlib
import matplotlib.pyplot as plt
from loadmodules import *


matplotlib.rcParams['text.usetex']=True
# matplotlib.rcParams['text.latex.preamble']=r"\usepackage{amsmath}"

matplotlib.rcParams['text.latex.preamble'] = r"""
\usepackage{amsmath}
\renewcommand{\rmdefault}{\sfdefault}
"""

# Set font size
plt.minorticks_on()
plt.rcParams.update({'font.size': 25,
                    'axes.linewidth': 2.5,
                    'axes.edgecolor': 'black',
                    'xtick.major.width': 1.5,
                    'xtick.minor.width': 1.5,
                    'ytick.major.width': 1.5,
                    'ytick.minor.width': 1.5,
                    'xtick.major.size': 10,
                    'xtick.minor.size': 7,
                    'ytick.major.size': 10,
                    'ytick.minor.size': 7,
                    'xtick.direction': 'inout',
                    'xtick.direction': 'inout',
                    'ytick.direction': 'inout',
                    'ytick.direction': 'inout',
                    'xtick.minor.visible': True,
                    'ytick.minor.visible': True,
                    'xtick.top': True,
                    'ytick.right': True})
plt.close('all')

# set axis color to black
plt.rcParams['text.color'] = 'black'

# suppress warnings when invoking plt.tight_layout() and using cax = fig.add_axes([0.17, 0.85, 0.4, 0.04])
with warnings.catch_warnings():
    warnings.simplefilter("ignore", UserWarning)
    plt.tight_layout()
    
    
# define good colors for plotting
mycyan = "#00A088"    