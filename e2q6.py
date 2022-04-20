import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile
import urllib

from IPython.display import Audio


url = "https://www.nasa.gov/62284main_onesmall2.wav"
Audio(url)

# Can't continue as can't get audio to play correctly

#convert to np array, fourier transform, cut off low and high frequencies
#convert back into time domain and play

