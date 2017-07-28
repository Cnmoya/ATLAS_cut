import subprocess as sp
from astropy.io import fits
from aplpy import make_rgb_image
import os
def read_montage_table():	
"""
Read Montage's Imgtbl and returns a list of dictionaries, one for each filter.
"""	
	files_dict = []
	return files_dict

def make_rgb():
"""
Using aplpy, make a RGB PNG image.
"""
	pass


def call_swarp():
"""
Calls swarp, iterating over the list of dicts.
"""
	pass

def make_image_cube():
"""
Stack the image for each band,creating a data cube with NAXIS3 = 5 
"""
	pass

def make_weight_cube():
"""
Stack the weight maps for each band.
"""
	pass

def get_header_keys():
"""
Save important keywords from pre-swarp input files headers.
"""
	header_dict = {}
	return header_dict
