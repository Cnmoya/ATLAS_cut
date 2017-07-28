import os
import sys
from astropy.io import fits
import numpy as np
import glob
import aplpy
from math import ceil
ugriz="ugriz"
id=sys.argv[1]
ra = sys.argv[2]
dec = sys.argv[3]
sizepix = int(ceil(float(sys.argv[4])/0.213))
ugriz_out = fits.HDUList()
ugriz_array = {'u':'u','g':'g','r':'r','i':'i','z':'z'}
for i in ugriz:
	if len(glob.glob('{}/*.fit'.format(i))) == 0:
		os.chdir(i)
		os.system('mHdr "{} {}" {} out.hdr'.format(ra,dec,sizepix))
		data = np.zeros((sizepix,sizepix))
		header = fits.Header.fromtextfile('out.hdr')
		header["DATAOK"] = (0,"No image found on server")
		header["FILT"] = i
		ugriz_out.append(fits.ImageHDU(data,header))
		os.chdir('..')
		ugriz_array[i]=''
	else:
		os.chdir(i)
		command = "swarp *.fit -c /data/cnmoya/script/ugriz.swarp -IMAGEOUT_NAME {} -CENTER {},{}".format(i+".fits",str(ra),str(dec)) + " -IMAGE_SIZE %f" %sizepix
		os.system(command)
		head = fits.getheader('{}.fits'.format(i))
		head["DATAOK"] = 1
		head["FILT"] = i
		head["FILES"] = ','.join([k for k in glob.glob('*.fit')])
		ugriz_out.append(fits.ImageHDU(fits.getdata('{}.fits'.format(i)),head))
		os.chdir("..")
ugriz_out.writeto('{}.fits'.format(id))
colors = [i for i in ugriz if ugriz_array[i]!='']

colors_0 = [i+'/'+i+'.fits' for i in colors[:3]]
colors_1 = [i+'/'+i+'.fits' for i in colors[-3:]]
aplpy.make_rgb_image(colors_0[::-1],"{}_{}{}{}.png".format(id,colors[0],colors[1],colors[2]))
aplpy.make_rgb_image(colors_1[::-1],"{}_{}{}{}.png".format(id,colors[-3],colors[-2],colors[-1]))
