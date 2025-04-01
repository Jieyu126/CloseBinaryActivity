from astropy.coordinates import Galactic, ICRS, Galactocentric, SkyCoord
from astropy.io import votable, ascii, fits
from astropy.stats import sigma_clip as sigmaclip
from astropy.table import Table
from astropy.timeseries import LombScargle
from astropy_healpix import HEALPix
# from astroquery.gaia import Gaia
# from astroquery.mast import Catalogs, Observations
# from astroquery.simbad import Simbad
# from astroquery.vizier import Vizier
from collections import deque
# from dustmaps.bayestar import BayestarQuery
# from dustmaps.sfd import SFDQuery
# from gaiaxpy import PhotometricSystem, load_additional_systems, generate
from importlib import reload
from IPython.display import Image, display
from itertools import permutations
from lmfit import Minimizer, Parameters, report_fit, Model, minimize
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import AutoMinorLocator
from matplotlib.backends.backend_agg import FigureCanvas
from multiprocessing.dummy import Pool as ThreadPool
from scipy import signal
from scipy.integrate import trapz

from scipy.interpolate import griddata
from scipy.signal import find_peaks
from scipy.signal import savgol_filter
from scipy.stats import gaussian_kde
from uncertainties import unumpy
from uncertainties.unumpy import log10
from urllib.parse import quote as urlencode
from urllib.request import urlretrieve
# import asfgrid
import astropy.coordinates as coords
import astropy.units as u
import astropy.units as units
import cmasher as cmr
import copy
import glob, glob2
# import h5py
# import healpy as hp
# import http.client as httplib 
# import import_ipynb
# import jason
# import kepler
# import lightkurve as lk
import math
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
# import progressbar
# import pylab
# import pysftp
# import pyvo
# import re
# import requests
# import shutil  # Module for file operations
# import subprocess
import sys
import time
import uncertainties
import warnings


pd.set_option('display.max_columns', None)
