import argparse
from sub import *
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


if __name__ == '__main__':
	if os.path.exists(cwd+"/{}".format(args.id)):
		os.system("rm -r {} ".format(args.id))

	os.system('mkdir {}'.format(args.id))

	os.chdir(args.id)
	map_file='/home/cnmoya/Desktop/tbls/maps/map_file.tbl'
	os.system('cat $map_file | parallel mCoverageCheck {}  {/.}.imglist  -point %3.6f %3.6f'%(args.RA,args.DEC))
	file_dict = read_montage_table()

	if args.keys:
		get_header_keys(file_dict,args.keys)

	 

	files_dict = imcopy(file_dict)

	call_swarp(files_dict,args.RA,args.DEC,args.size)


	make_image_cube(_id,headers=args.keys)
	make_weight_cube(_id)








	if args.png:
		make_rgb(args.id,files_dict)
