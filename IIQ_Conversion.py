# Converts all IIQ files from input folder to TIFF and stores them
# in an output folder. Make sure to manually copy the Capture One
# folder, .DS_Store file, and the captureProgramLog to the new folder
# if you are moving files

import os
import rawpy
import cv2

# Input directory path (relative to current folder)
directory_in_string = "G:/Julia/TrezonaW2D/Capture2"
# Output directory path (relative to current folder)
directory_out_string = "G:/Julia/TrezonaW2D/Output"
# Parsed directory path
directory = os.fsencode(directory_in_string)

file_list = os.listdir(directory)
len = len(file_list) - 3
progress = 0

# Iterates through all IIQ files in input folder and saves them as TIFF
# to output folder: Uses rawpy to read and cv2 to write, with os for
# name manipulation
for file in file_list:
    filename = os.fsdecode(file)
    firstName, extension = os.path.splitext(os.path.basename(filename))
    if extension == ".IIQ":
        progress = progress + 1
        print("File " + str(progress) + " of " + str(len) + ":\n" + filename)
        rawpyRead = directory_in_string + "/" + filename
        with rawpy.imread(rawpyRead) as raw:
            img = raw.postprocess()
        cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        outName = directory_out_string + "/" + firstName + ".TIFF"
        cv2.imwrite(outName,img)

print("Done")