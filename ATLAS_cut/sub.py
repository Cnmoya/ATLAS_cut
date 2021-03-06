import  subprocess as sp
from astropy.io import fits
from aplpy import make_rgb_image
import os
from functools import reduce
from multiprocessing import Pool
from math import ceil




def read_montage_table():	


    """
    Read Montage's Imgtbl and returns a list of dictionaries, one for each filter.

    """
    files_dict = {'u':[],'g':[],'r':[],'i':[],'z':[]}
    files = sp.check_output("awk '{print $NF}' *.imglist | grep _st",shell=True).decode("UTF-8").strip().split('\n')
    for i in files:
        _dict = parse_path(i)
        files_dict[_dict["filter"]].append(_dict['file'])


    return files_dict

def make_rgb(files_dict):

    """
    Using aplpy, make a RGB PNG image.
    """
    pass


def call_swarp(file_dict,ra,dec,size,sizepix = 0.213):
    """
    Calls swarp, iterating over the list of dicts.
    """
    pix = ceil(size/0.213)
    def swarp(_tuple):
        if _tuple[1]!=[]:
            os.system("swarp {} -c default.swarp -IMAGEOUT_NAME {}.fits -WEIGHOUT_NAME {}.w -CENTER{},{} -IMAGE_SIZE {}".format(" ".join(_tuple[1]),_tuple[0],_tuple[0],ra,dec,pix))
        else:
            os.system('mHdr "{} {}" {} out.hdr'.format(ra,dec,size))
            data = np.zeros((pix,pix))
	    header = fits.Header.fromtextfile('out.hdr')
	    header["DATAOK"] = (0,"No image found on server")
            fits.writeto("{}.fit".format(_tuple[0]),data=data,header=header)

    p = Pool(5)
    p.map(swarp,[_tuplex for _tuplex in file_dict.items()])

def make_image_cube(_id):
    """
    Stack the image for each band,creating a data cube with NAXIS3 = 5 
    """
    ugriz_out = fits.HDUList()
    for i in 'ugriz':
        head = fits.getheader('{}.fit'.format(i))
        if not "DATAOK" in header.keys():
            head["DATAOK"] = 1
	head["FILT"] = i
	ugriz_out.append(fits.ImageHDU(fits.getdata('{}.fit'.format(i)),head))
    ugriz_out.writeto('{}.fits'.format(_id))


def make_weight_cube():
    """
    Stack the weight maps for each band.
    """
    pass

def get_header_keys(files_dict,keys):
    """
    Save important keywords from pre-swarp input files headers.
    """
    for i in files_dict.keys():
        cont = 1
        with open('%s.hdr'%i,'w') as out_hdr:
            for _file in files_dict[i]:
                output = sp.check_output("dfits {} | egrep '{}' ".format(_file,'|'.join(keys)),shell=True).decode('UTF-8')
                output = reduce(lambda s, kv: s.replace(kv,kv+'00{}'.format(cont),),keys,output)
                out_hdr.write(output)
                cont+=1

        out_hdr.close()
def parse_path(path):
    """
    Recieves a path to a header file and returns a dict with keys filter and files.
    """ 
    file_dict = {}
    _path = path.split("/")
    file_dict["filter"] = _path[-2][-1]
    file_dict["file"] = "/data/atlas_exposed/nightlies/"+_path[-1][4:14] +"/"+_path[-1][3:-3]+"fit"+"[{}]".format(_path[-1][0:2])
    return file_dict

