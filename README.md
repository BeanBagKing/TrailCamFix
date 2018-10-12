# TrailCamFix
Changes file names for Foxelli (and other?) trail cameras to include date/time

# About
When Foxelli trail cameras take a pictures/video, it takes two pictures and a video by default. the files are named as follows:
DSCF0001.JPG
DSCF0002.JPG
DSCF0003.AVI
DSCF0004.JPG
etc...

So the first 3 are from one motion event. Numbers 4, 5, and 6 would be from the next, and so forth. When you move these off of the camera, it starts over again at 1. In other words, the numbering is based on the files on disk, and not shutter count. If you move multiple batches off you end up with DSCF0001.JPG, DSCF0001 - Copy.JPG, DSCF0001 - Copy - Copy.JPG and so forth. In addition to creating an unreadable mess, you're also lost as to where you are in your timeline. 

The purpose of this script was to take the timestamp from the exifdata in the photos and use that to rename the files, providing a more organized file structure that will not have name conflicts. However, I discovered that the video files (AVI) don't have this metadata. Therefore, I...

```
Find the AVI files
Strip out the number
Back up one (getting the previous file, a JPG)
Get the timestamp from that
Increment by 1 second (to avoid name conflicts)
Rename the AVI (and, since I have it anyway, add the metadata)
Then rename all the images
```

# Requirements
```
pip install exifread
pip install image
apt install exiftool
apt install ffmpeg
```
