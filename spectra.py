#/usr/bin/env python3
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
class Spectrum(object):
	def __init__(self,filename=None):
		self.filename=filename
		with fits.open(self.filename) as f:
			self.f = f
		
	@property
	def hdu_lengths(self):
		header_length=len(self.f)
		return(header_length)
		
	@property
	def ra(self):
		ra=self.f[0].header["RA"]
		return(ra)
		
	@property
	def dec(self):
		dec=self.f[0].header["DEC"]
		return(dec)
		
		
	@property
	def plate(self):
		plate=self.f[0].header["NAME"]
		return(plate)
		

	@property	
	def flux(self):
		with fits.open(self.filename) as f:
			self.f=f
			flux=np.zeros(4606)
			for k in range(4606):
				flux[k]=self.f[1].data[k][0]
		return(flux)
		
	
	@property	
	def wavelength(self):
		with fits.open(self.filename) as f:
			self.f=f
			wavelength=np.zeros(4606)
			for k in range(4606):
				wavelength[k]=self.f[1].data[k][1]
		return(wavelength)
				
		
		
		
		
		
		
