# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:40:10 2020
The lTSpice file newneuron.asc is run thyough the python commands and plotted using python 
@author: PRATT
"""
import numpy as np
from apply_ltspice_neuron import apply_ltspice_neuron 
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
sample_width=10e-3    # our samples shall be 10 ms wide
delta_t=1e-6          # time step between samples: 1 us
samples = int(sample_width/delta_t)

time = np.linspace(0,sample_width,samples)

# we want 1.9 V till 9 ms
signal_a = 0+ 1.9 * ((time < 9e-3))

##################################################
##        apply neuron - configuration 1        ##
##################################################

# all values in SI units
configuration_1 = {
  "C":850e-12, # 850 pF
  "R":0.82e6   # 820 kOhm
}

dummy, signal_b1 = apply_ltspice_neuron(
      "newneuron.asc",
      time, signal_a,
      params=configuration_1
      )
peaks,_ =find_peaks(signal_b1,height=1.5)
p=len(peaks)
print(p/0.01,"Hz is the frequency of output")


##################################################
##           plot input vs output(s)            ##
##################################################
  
plt.plot(signal_a, label="signal_a (LTSpice input)")
plt.plot(signal_b1,label="signal_b1 (LTSpice output, C=850pF, V= 1.9V)")
plt.plot(peaks, signal_b1[peaks], "x")
plt.xlabel("time (s)")
plt.ylabel("voltage (V)")
plt.ylim((-1,3.5))

plt.legend()
plt.show()

