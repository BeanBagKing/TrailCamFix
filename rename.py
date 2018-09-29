#!/usr/bin/python

import sys, os, exifread, datetime
from PIL import Image

for filename in os.listdir('.'):
  if 'AVI' in filename:
    filenum = ''.join(i for i in filename if i.isdigit())		# The number of the file, we'll need this to decrement by 1 to get the file before it
    copyfrom = int(filenum)-1 									# This is the file number we want to copy our exif time from
    copyfromfilename = "DSCF" + str(copyfrom).zfill(4) + ".JPG" # This is the file name we want to copy our exif time from

    f = open(copyfromfilename, 'rb')
    tags = exifread.process_file(f, details=False, stop_tag='DateTimeOriginal') # Get the tags we need
    date = tags.get('EXIF DateTimeOriginal')									# Get the exact tag we need
    date = datetime.datetime.strptime(str(date), '%Y:%m:%d %H:%M:%S')			# Convert the tag to python datetime
    date = date + datetime.timedelta(0,1) 										# Add 1 second, so we don't have two files with the same timestamp
    date = date.strftime('%Y%m%d_%H%M%S')										# Convert our date into the format we want for our file name

    print("Working on AVI #" + str(filenum).zfill(4))
    os.system("ffmpeg -loglevel quiet -i " + filename + " -codec copy -metadata ICRD=\"2018-09-23 13:06:11\" " + date + ".AVI") # Create proper file
    os.remove(filename)	# Remove the original

    # ---- Samples ----
    # DSCF0070.AVI
    #'EXIF DateTimeOriginal': (0x9003) ASCII=2018:09:21 16:35:35 @ 748
    # Date/Time Original              : 2018:09:23 13:06:10
	# Create Date                     : 2018:09:23 13:06:10
	# exiftool -ext JPG '-FileName<CreateDate' -d %Y%m%d_%H%M%S%%-c.%%e .
	# ffmpeg -loglevel quiet -i DSCF0070.AVI -codec copy -metadata ICRD="2018-09-23 13:06:11" out.avi

print("Finished AVIs, fixing JPGs") # exiftool can't write to AVIs, and apparently you have to create a new file for writing to AVIs
os.system("exiftool -ext jpg '-FileName<CreateDate' -d %Y%m%d_%H%M%S%%-c.%%e .") # It can write to JPG though, so those are super easy.
print("FINISHED!")
