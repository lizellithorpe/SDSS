#/usr/bin/env python3
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
class Spectrum(object):
	def __init__(self,filename=None):
		self.filename=filename
		with fits.open(self.filename) as f:
			self.f = f
		self.emit=None
		self.absorb=None
		
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
			length=self.f[1].header["NAXIS2"]
			flux=np.zeros(length)
			for k in range(length):
				flux[k]=self.f[1].data[k][0]
		return(flux)
		
	
	@property	
	def wavelength(self):
		with fits.open(self.filename) as f:
			self.f=f
			length=self.f[1].header["NAXIS2"]
			wavelength=np.zeros(length)
			for k in range(length):
				wavelength[k]=10**self.f[1].data[k][1]
		return(wavelength)
	
		
	def findlines(self):
		wavelength=self.wavelength
		flux=self.flux
		
		from astropy.modeling import models
		import astropy.units as u
		from specutils import Spectrum1D, SpectralRegion
		from specutils.manipulation import noise_region_uncertainty
		from specutils.fitting import find_lines_threshold
		
		spectrum=Spectrum1D(flux=flux*u.Jy,spectral_axis=wavelength*u.Angstrom)
		noise_region=SpectralRegion(3000*u.Angstrom,10000*u.Angstrom)
		spectrum=noise_region_uncertainty(spectrum,noise_region)
		
		lines=find_lines_threshold(spectrum, noise_factor=4)
		
		emit=lines['line_type']=='emission'
		absorb=lines['line_type']=='absorption'
		
		emission_lines=lines['line_center'][emit]
		
		try:
			emission_lines_arr=np.zeros(len(emission_lines))
		except TypeError:
			print('no emission lines!')
			emission_lines_arr=None
			emission_lines=None
		
		if emission_lines is not None:
			for i in range(len(emission_lines)):
				emission_lines_arr[i]=emission_lines.data[i]
			
		absorption_lines=['line_type']=='absorption'
		
		try:
			absorption_lines_arr=np.zeros(len(absorption_lines))
		except TypeError:	
			print('no absorption lines!')
			absorption_lines_arr=None
			absorption_lines=None
		
		if absorption_lines is not None:
			for j in range(len(absorption_lines)):
				absorption_lines_arr[j]=absorption_lines.data[j]
			
		self.emit=emission_lines_arr
		self.absorb=absorption_lines_arr
		
		return(emission_lines_arr,absorption_lines_arr)
		
		
	
				
		
		
		
		
		
		
