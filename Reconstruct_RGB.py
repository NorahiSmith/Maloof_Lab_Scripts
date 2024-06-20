import cv2
import os

blue_folder = 'G:/Julia/TrezonaW2D/ColorBalance/cap78754_470nm/'
green_folder = 'G:/Julia/TrezonaW2D/ColorBalance/cap78755_530nm/'
red_folder = 'G:/Julia/TrezonaW2D/ColorBalance/cap78756_670nm/'
output_folder = 'G:/Julia/TrezonaW2D/ColorBalance/final/'

blue_dir = os.fsencode(blue_folder)
green_dir = os.fsencode(green_folder)
red_dir = os.fsencode(red_folder)

blue_list = os.listdir(blue_dir)
green_list = os.listdir(green_dir)
red_list = os.listdir(red_dir)

for i in range(0, len(blue_list), 3):
    blue = cv2.imread(blue_folder + str(blue_list[i])[2:19], cv2.IMREAD_GRAYSCALE)
    print(blue_folder + str(blue_list[i])[2:19])
    green = cv2.imread(green_folder + str(green_list[i+1])[2:19], cv2.IMREAD_GRAYSCALE)
    print(green_folder + str(green_list[i+1])[2:19])
    red = cv2.imread(red_folder + str(red_list[i+2])[2:19], cv2.IMREAD_GRAYSCALE)
    print(red_folder + str(red_list[i+2])[2:19])
    output = cv2.merge((blue, green, red))

    filename = os.fsdecode(blue_list[i])
    firstName, extension = os.path.splitext(os.path.basename(filename))
    out_path = output_folder + firstName + '.jpg'
    cv2.imwrite(out_path, output)
