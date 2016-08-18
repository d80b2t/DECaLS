#!/usr/bin/python

"""
Some baby code just to start to play around with FITS files in Python and AstroPy and
make some QSO color-color plots... ;-)
"""

"""
Links to FITS resources:
  http://docs.astropy.org/en/stable/io/fits/
  http://www.astropy.org/astropy-tutorials/FITS-images.html
  https://python4astronomers.github.io/astropy/fits.html
  https://gist.github.com/phn/3054997
  http://www.astropython.org/tutorials/pyfits-fits-files-in-python93/
"""

import numpy
import matplotlib.pyplot as plt
import pyfits

# Set the path to, and the name of, your data FITS file 
data_path='/cos_pc19a_npr/data/DECaLS/'
data_file='decals-dr2-DR12Q.fits'

# 'data_full' just a variable name that NPR likes to use ;-)
data_full=data_path+data_file

# Reading in and seeing  the Header information
pyfits.info(data_full)

header_primary = pyfits.getheader(data_full)
list(header_primary.keys())


# Open, and get info on, the FITS file:
hdulist = pyfits.open(data_full)
hdulist.info()


# Okay, what we really want to do... ;-) 
data_table = pyfits.getdata(data_full)

# Quick check on the format/dimensions of the FITS table file...
print(type(data_table),'\n')
print('The number of rows of is.... ', data_table.shape,'\n')
print('The number of columns is...  ', len(data_table.names),'\n\n')


## Interograting the FITS file...
# First row
print(data_table[0])

# First column
print(data_table.field(0))

# First row, First column
print(data_table[0][0])

# Names of individual columns
print(data_table.names, '\n\n')

##
## Now getting into it some more...
##

decam_flux = data_table.field('DECAM_FLUX')

print(numpy.ndarray.max(decam_flux))

numpy.histogram(decam_flux)

plt.hist(decam_flux, bins='auto')
plt.show()

