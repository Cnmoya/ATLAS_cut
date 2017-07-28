#!/bin/bash
#create_filter_list.sh
touch  u_files.imglist
touch  g_files.imglist
rm r_files.imglist
rm i_files.imglist
rm z_files.imglist
for line in $(ls /data/atlas_exposed/nightlies/*/**_st.fit) 
do
	if [ "$(dfits $line | grep 'FILT1 NAME')" == "HIERARCH ESO INS FILT1 NAME  = 'u_SDSS  '   / Filter name." ]
	
	then
		echo $line >> u_files.imglist
	
	elif [ "$(dfits $line | grep 'FILT1 NAME')" == "HIERARCH ESO INS FILT1 NAME  = 'g_SDSS  '   / Filter name." ]
	
	then
		echo $line >> g_files.imglist		
	
	elif [ "$(dfits $line | grep 'FILT1 NAME')" == "HIERARCH ESO INS FILT1 NAME  = 'r_SDSS  '   / Filter name." ]
	
	then
		echo $line >> r_files.imglist
	
	elif [ "$(dfits $line | grep 'FILT1 NAME')" == "HIERARCH ESO INS FILT1 NAME  = 'i_SDSS  '   / Filter name." ]
	
	then
		echo $line >> i_files.imglist
	
	elif [ "$(dfits $line | grep 'FILT1 NAME')" == "HIERARCH ESO INS FILT1 NAME  = 'z_SDSS  '   / Filter name." ]
	
	then
		echo $line >> z_files.imglist

	fi
done	
#end of script
