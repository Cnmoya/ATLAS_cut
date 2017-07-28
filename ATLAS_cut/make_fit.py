import sys
from astropy.io import fits
import os
 
head = sys.argv[1]
if "hdr" in head:
	hdr  = head.split("/")[-1]
	fname = '/data/atlas_exposed/nightlies/'+hdr.split("_")[1][1:]+'/'+hdr[3:].replace('hdr',"fit")
	hdu = int(head.split("/")[-1].split("_")[0])
	header = fits.Header.fromtextfile(head)
	filt = head.split("/")[-2][-1]
	os.chdir(filt)
	out_data = fits.getdata(fname,hdu)
	fits.writeto(hdr.replace("hdr","fit"),out_data,header)
	#os.system("cp {} {}".format(head,hdr)
	#command = "swarp '{}' -c /home/cnmoya/script/ugriz.swarp  -IMAGEOUT_NAME {}  -CENTER {},{}".format(hdr.replace('hdr','fit'),hdr.replace('hdr','fits'),str(ra),str(dec)) + " -IMAGE_SIZE %f" %sizepix
	#print(command)	
	#os.system(command)

#data = fits.getdata(fname,hdu)
#out = fits.writeto(head.split("/")[-2][-1]+'/'+str(hdu)+"_"+fname.split("/")[-1],data,header)



