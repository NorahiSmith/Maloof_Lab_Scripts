import os
import csv
import numpy as np

image_logs_dir_string = "G:/Julia/TrezonaW2D/image_logs/"
image_logs_dir = os.fsencode(image_logs_dir_string)

tiff_directory_string = ""
tiff_dir = os.fsencode(tiff_directory_string)

file_name_index = 0
im_wavelength_index = 1
sample_imaged_index = 2

image_log = []

for file in os.listdir(image_logs_dir):
    filename = os.fsdecode(file)
    with open(image_logs_dir_string + filename, newline = '') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row == ['file_name', 'im_wavelength', 'sample_imaged']:
                continue
            image_log.append(row)

# image_log = np.array(image_log)

for file in os.listdir(tiff_dir):
    filename = os.fsdecode
    firstName, extension = os.path.splitext(os.path.basename(filename))
    index = image_log.index(firstName + ".IIQ")

