import cv2
import os

input_folder = 'G:/Julia/TrezonaW2D/Output/cropped-photos/'

dir = os.fsencode(input_folder)

for file in os.listdir(dir):
    filename = os.fsdecode(file)
    img = cv2.imread(input_folder + filename)
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('Image', img)
    cv2.waitKey(4000)
    cv2.destroyAllWindows