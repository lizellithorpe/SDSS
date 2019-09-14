#/usr/bin/env python3
import sys
sys.path.append("/Users/lizellithorpe/desktop/SciCoder-2019-Keck/Data Files/spectra/sdss_module")

from sdss_module.spectra import Spectrum

s=Spectrum(filename='spec-4055-55359-0010.fits')
print(s.filename)
print("==================")
print("Right Ascension:"+str(s.ra))
print("==================")
print("Declination:"+str(s.dec))
print("==================")
print("Plate Name:"+str(s.plate))


import matplotlib.pyplot as plt

import numpy as np



s.findlines()

plt.plot(s.wavelength,s.flux)
if s.emit is not None:
	for value in s.emit:
		plt.axvline(value, ymin=0, ymax=10, color='red', linestyle='--')
		plt.xlabel('Wavelength [A]')
		plt.ylabel('Flux')
		plt.title(s.filename+' w/ identified emission lines')
		
	
if s.absorb is not None:
	for value in s.absorb:
		plt.axvline(value, ymin=0, ymax=10, color='green', linestyle='--')

	
print(s.flux_norm)
plt.show()

plt.plot(s.flux_norm)
plt.xlabel('Wavelength [A]')
plt.ylabel('Flux')
plt.title(s.filename +'(normalized)')
plt.show()