#!/bin/bash
#make_headers.sh
img_file='/home/cnmoya/Desktop/tbls/filter_lists.tbl'
cat $img_file | parallel python create_all_headers.py {}
#end of script
