import argparse
import os

parser = argparse.ArgumentParser(description="Obtain a cutout from the ATLAS database,returns a FITS file with 5 image extensions, one for each filter (ugriz).")
parser.add_argument("id",type=str,help="prefix for the output FITS file (id.fits).")
parser.add_argument("RA",type=float,help="Right Ascension in decimals.")
parser.add_argument("DEC",type=float,help="Declination in decimals.")
parser.add_argument("size",type=int,help="Size of the cutout in arcseconds.")
parser.add_argument("-r","--rgb",dest="png",action='store_const',const=True,default=False,help="Aditionally, make a pair of PNG images.")
parser.add_argument("-p","--pixelscale",metavar="Scale",dest="pixsize",default='0.213',type=float,help="Pixel scale, default is set to 0.213 arcseconds per pixel")
parser.add_argument("-k","--keys",dest="keys",metavar="keys",nargs="+",type=str,help="Header keywords to propagate from swarp input files.",default=False)
args=parser.parse_args()
cwd = os.getcwd()
print(args.keys)
#if os.path.exists(cwd+"/%s"%s):
	#os.command("rm -r %s"%s)

#else:
	#os.command('mkdir %s'%s)


#map_file='/home/cnmoya/Desktop/tbls/maps/map_file.tbl'
#os.command('cat $map_file | parallel mCoverageCheck {}  {/.}.imglist  -point $ra $dec')















if args.png:
	pass
