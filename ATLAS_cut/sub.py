import  subprocess as sp
from astropy.io import fits
from aplpy import make_rgb_image
import os
from functools import reduce
from multiprocessing import Pool
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

def make_rgb():
    """
    Using aplpy, make a RGB PNG image.
    """
    pass


def call_swarp(file_dict):
    """
    Calls swarp, iterating over the list of dicts.
    """
    os.system("swarp -c default.swarp")
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

def get_header_keys(files_dict,keys):
    """
    Save important keywords from pre-swarp input files headers.
    """
    for i in files_dict.keys():
        cont = 0
        with open('%s.hdr'%i,'w') as out_hdr:
            for _file in files_dict[i]:
                output = sp.check_output(" egrep '{}' {}".format('|'.join(keys),_file),shell=True).decode('UTF-8')
                reduce(lambda s, kv: s.replace(kv,kv+'00{}').format(cont), keys, output)
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

