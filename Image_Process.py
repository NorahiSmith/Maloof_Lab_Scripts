# Takes as input a folder full of unsorted .IIQ (or other extension) files. Converts all .IIQs to 
# a file format of your choice and saves all grayscale images sorted by wavelength in folders in
# the output directory. Converts images to color (with modifiable RGB scaling) and saves them
# in specified folder. Crops images based on user input (click the top and bottom of a square,
# then click the center in the x plane) and saves cropped images to a folder in output.
# Make sure that the directory_out_string folder and the directory_out_string_color
# folder exist before running the script.
# Assumptions:
# Every image has either all red, green, and blue components or none of them
# Color images will not be overwritten (change this around line 130 if needed)
# Red, green, and blue wavelengths are in the wavelengths array  

import os
import rawpy
import cv2
import csv
import matplotlib.pyplot as plt

# Make sure all of the following values are correct before running:
# ------------------------------------------------------------------------------------- #
# Input directory path
directory_in_string = "G:/Julia/Norah_Stuff/Capture/"
# Output directory path for greyscale images
directory_out_string = "G:/Julia/Norah_Stuff/Output/"
# Output directory path for color images
directory_out_string_color = "G:/Julia/Norah_Stuff/Output/rgb/"
# Output directory for cropped images
directory_out_string_crop = "G:/Julia/TrezonaW2D_2/Output/cropped"
# Wavelengths used
wavelengths = ["365", "470", "530", "670", "740"]
# RGB Wavelengths
red_wav = "670"
green_wav = "530"
blue_wav = "470"
# RGB Color Scaling (<= 1)
red_scale = 0.9
green_scale = 1
blue_scale = 0.9
# RGB Size Scaling
im_scale = 0.7
# Folder with Image Logs
image_logs_dir_string = "G:/Julia/Norah_Stuff/image_logs/"
# Input Extension
in_ext = ".IIQ"
# Grayscale output Extension
out_ext_gray = ".TIFF"
# Color output Extension
out_ext_color = ".jpg"
# ------------------------------------------------------------------------------------- #

# Create Image Log dictionary (lookup table): filename: [wavelength, sample_name]
image_log_dict = {}
# Create lookup table for image_sampled: sample_name: [filename, wavelength]
strat_log_dict = {}

image_logs_dir = os.fsencode(image_logs_dir_string)
for file in os.listdir(image_logs_dir):
    filename = os.fsdecode(file)
    with open(image_logs_dir_string + filename, newline = '') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row == ['file_name', 'im_wavelength', 'sample_imaged']:
                continue
            image_log_dict[row[0]] = [row[1], row[2]]
            strat_log_dict[row[2]] = [row[0], row[1]]

# Beginning of file type conversion and sorting
in_directory = os.fsencode(directory_in_string)
file_list = os.listdir(in_directory)
length = len(file_list) - 3
progress = 0

# Creates new directory for gray output if none exists
if not os.path.exists(directory_out_string):
    os.makedirs(directory_out_string)

# Creates new directories for all wavelengths
for wav in wavelengths:
    newpath = directory_out_string + wav
    if not os.path.exists(newpath):
        os.makedirs(newpath)

# Creates new directory for color output if none exists
if not os.path.exists(directory_out_string_color):
    os.makedirs(directory_out_string_color)

# Iterates through all IIQ files in input folder and saves them as TIFF
# to output folder with specified wavelength: Uses rawpy to read and cv2 to write, with os for
# name manipulation
# for file in file_list:
#     filename = os.fsdecode(file)
#     firstName, extension = os.path.splitext(os.path.basename(filename))
#     if extension == in_ext:
#         progress = progress + 1
#         print("Converting File " + str(progress) + " of " + str(length) + ":\n" + filename)

#         sample_name = image_log_dict.get(filename)
#         if (sample_name == None):
#             print("Sample was not saved to logs. Continuing...")
#             continue
#         sample_wav = sample_name[0]
#         sample_name = sample_name[1]
#         outName = directory_out_string + sample_wav + "/" + sample_name + "_" + sample_wav + "_" + firstName + out_ext_gray
#         print(outName)
#         if os.path.exists(outName):
#             print("Path already exists. Image not overwritten")
#             continue

#         rawpyRead = directory_in_string + filename
#         if not os.path.exists(rawpyRead):
#             print("Image does not exist")
#             continue
#         with rawpy.imread(rawpyRead) as raw:
#             img = raw.postprocess()

#         # cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         cv2.imwrite(outName,img)
            

# Creates RGBs from wavelengths
red_path = directory_out_string + red_wav
blue_path = directory_out_string + blue_wav
green_path = directory_out_string + green_wav

red_dir = os.fsencode(red_path)
red_list = os.listdir(red_dir)
green_dir = os.fsencode(green_path)
green_list = os.listdir(green_dir)
blue_dir = os.fsencode(blue_path)
blue_list = os.listdir(blue_dir)

red_list_len = len(red_list)

for i in range(red_list_len):
    red_name = os.fsdecode(red_list[i])
    green_name = os.fsdecode(green_list[i])
    blue_name = os.fsdecode(blue_list[i])

    print("Creating rgb File " + str(i+1) + " of " + str(red_list_len) + ": " + red_name)

    out_name = red_name.split(sep = "_")
    out_name = out_name[0] + "_" + out_name[1] + out_ext_color
    # out_name = out_name[0] + "_" + out_name[1] + "_" + out_name[2] + out_ext_color
    out_path = directory_out_string_color + out_name

    if os.path.exists(out_path):
        print("Path already exists. Image not overwritten")
        continue

    red = cv2.imread(red_path + "/" +  red_name, cv2.IMREAD_GRAYSCALE)
    green = cv2.imread(green_path + "/" +  green_name, cv2.IMREAD_GRAYSCALE)
    blue = cv2.imread(blue_path + "/" +  blue_name, cv2.IMREAD_GRAYSCALE)

    red = (red * red_scale).astype(int)
    green = (green * green_scale).astype(int)
    blue = (blue * blue_scale).astype(int)

    img_color = cv2.merge((blue, green, red))
    width =  int(img_color.shape[1] * im_scale)
    height = int(img_color.shape[0] * im_scale)
    dim = (width, height)
    
    # resize image
    # resized = cv2.resize(img_color, dim, interpolation = cv2.INTER_AREA)

    cv2.imwrite(out_path, img_color)

# Crop Image to Square
if not os.path.exists(directory_out_string_crop):
    os.makedirs(directory_out_string_crop)

progress = 1
rgb_dir = os.fsencode(directory_out_string_color)
rgb_list = os.listdir(rgb_dir)
crop_len = len(rgb_list)
for file in rgb_list:
    filename = os.fsdecode(file)
    print("Cropping Image " + str(progress) + " of " + str(crop_len) + ":\n" + filename)
    progress = progress + 1
    output_name = newpath + "/" + filename
    if os.path.exists(output_name):
        print("File Already Cropped. Continuing...")
        continue

    img_uncropped = cv2.imread(directory_out_string_color + "/" + filename)
    print("Click on the top and bottom of the square you want to crop, then click on the center")
    plt.imshow(img_uncropped)
    top,bottom, center = plt.ginput(3)
    square_side = abs(top[1] - bottom[1]) / 2 
    square_center_y = min(top[1], bottom[1]) + (square_side)
    square_center_x = center[0]
    plt.close()
    if square_center_x - square_side < 0 | square_center_x +square_side > cv2.shape(img_uncropped)[1]:
        print("Center is too close to edges, changing square size")
        square_side = min(square_center_x, cv2.shape(img_uncropped)[1] - square_center_x)
    img_crop = img_uncropped[int(square_center_y - square_side):int(square_center_y + square_side), int(square_center_x - square_side):int(square_center_x + square_side)]
    
    cv2.imwrite(output_name, img_crop)

print("Done")