#!/usr/bin/env python

# This script will use the NCBI SRA Toolkit
# to download and process files from the
# https://www.ncbi.nlm.nih.gov/ site.

import subprocess as sp
import os


############ Initialize variables #################

# $srrFile contains the location of the the SRA Accession list
srrFile = "C:\\sra\\SRR_Acc_List.txt"
srrFileProc = "C:\\sra\\SRR_Acc_List.txt.processed"
# Here the failed downloads will be wriiten for further processing
srrFailedFile = "C:\\sra\\SRR_FailedDL_List.txt"
# Executable to run from the SRA Toolkit
# prefetch will get the files in SRA format
toolExe = "C:\\sra\\sratoolkit\\bin\\prefetch.exe"
# maximum download size argument for prefetch, use max size
arg_maxDLsize = "999G"
# path to the ascp executable and keyfile to enable downloads via Aspera Connect (instead of http)
arg_ascp = "c:\\Program Files (x86)\\Aspera\\Aspera Connect\\bin\\ascp.exe|c:\\Program Files (x86)\\Aspera\\Aspera Connect\\etc\\asperaweb_id_dsa.openssh"
# Location for the downloaded SRA files.
# This can be set with vdb-config from the SRA Toolkit (/path/to/toolkit/bin)
sraDlLocation = "D:\\ncbi\\sra"

#print(num_lines)

def sra_download():
    # get number of lines in SRA file
    num_lines = sum(1 for line in open(srrFile) if line.rstrip())
    # counter for number of processed lines in SRA file
    processed_files = 0
    # file handle fh
    fh = open(srrFile)
    #num_lines = sum(1 for line in fh if line.rstrip())
    while True:
        # read line
        line = fh.readline()
        # check if line is not empty
        if not line:
            break
        line = line.rstrip("\n")
        processed_files += 1
        print("\nNow processing ", processed_files, "of total ", num_lines)
        # SRA Toolkit file
        # print(line, toolExe, arg_maxDLsize, arg_ascp)
        sp.run([toolExe, "-X", arg_maxDLsize, "-a", arg_ascp, line])
    fh.close()



# Now rename the processed file to prevent processing again
#os.rename(srrFile, srrFileProc)


def sra_download_check():
    pass
 
# Check if all lines in the SRA file are downloaded
# Clean download directory of tmp and lock type files , delete all non .sra files
# Get all lines in the SRA file
# Get all of the downloaded files from the download directory, just the basename
# Get total lines in file and total lines downloaded
# Sort and compare the files
# Write out the difference
# Download the missing files listed in the difference file

def sra_file_check():
    pass

    # 
    # get sra file directory and check for sra file and/or failed file
    # if both 


def main():
    sra_file_check()
    sra_download()
    sra_download_check()


if __name__ == "__main__":
    main()
