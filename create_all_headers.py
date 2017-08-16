import astropy.io.fits as fits
import os
import numpy
import sys

#def fix_fits_file(f):
#	hdu = fits.open(f)
#	for i in range(len(hdu)-1):
#		i = i+1
#		output = path_headers+str(i-1).zfill(2)+'_'+f.split('/')[-1].replace('.fit','.hdr')
#		header_output = open(output,'w')
#		# change this function to the one given by astropy.io.fits.Header dump to text file
#		header_output.write(repr(hdu[i].header))
#		header_output.close()
#	
#	hdu.close()
#	return

def fix_fits_file(f):
	for i in range(1,33):
		output = path_headers+str(i).zfill(2)+'_'+f.split('/')[-1].replace('.fit','.hdr')
		head = fits.getheader(f,i)	
		head.totextfile(output, endcard=True, clobber=True)
#		header_output = open(output,'w')
		# change this function to the one given by astropy.io.fits.Header dump to text file
#		header_output.write(repr(hdu[i].header))
#		header_output.close()
	
	return

#files = glob.glob('/home/jgonzal/test/*')
files = open(sys.argv[1],'r')
next(files)
next(files)
path_headers = '/data/cnmoya/fixed_headers_{}/'.format(sys.argv[1].split("/")[-1].split("_")[0])
os.system('rm -f '+path_headers+'*.hdr')
for f in files:
	fix_fits_file(f.strip())

# if I remember well, I create the master_table3.dat instead of a master_table2.dat so I can still create plots while updating the databse.
# after completition, I need to mv the table3->table2
#montage.mCoverageCheck(in_table='scripts/master_table.dat', out_table='out_table',mode='circle',ra=323.0633096,dec=-31.1512561,radius=0.0001)

# 'master_table3.dat' will have all the good data.
