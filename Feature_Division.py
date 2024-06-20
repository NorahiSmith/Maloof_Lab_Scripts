import numpy as np
import os
from keras._tf_keras.keras.preprocessing import image
from  keras._tf_keras.keras.applications.vgg16 import VGG16
from keras._tf_keras.keras.applications.vgg16 import preprocess_input
from sklearn.cluster import KMeans
import cv2

model = VGG16(weights = 'imagenet', include_top = False)
model.summary()

dir_in_string = "G:/Julia/TrezonaW2D/Output/Final_Cropped/"
dir_out_string = "G:/Julia/TrezonaW2D/Output/Grouping/"

if not os.path.exists(dir_out_string):
    os.makedirs(dir_out_string)

img_feature_list = []
in_dir = os.fsencode(dir_in_string)
for file in os.listdir(in_dir):
    filename = os.fsdecode(file)
    file_path_string = dir_in_string + filename

    img = image.load_img(file_path_string)
    img = image.smart_resize(img, (224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis = 0)
    img_data = preprocess_input(img_data)

    img_feature = model.predict(img_data)
    img_feature_np = np.array(img_feature)
    img_feature_list.append(img_feature_np.flatten())

img_feature_list_np = np.array(img_feature_list)
kmeans = KMeans(n_clusters = 10, random_state = 0).fit(img_feature_list_np)
print(kmeans.labels_)

for i in range(5):
    newpath = dir_out_string + str(i)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

indices = kmeans.labels_
files = os.listdir(in_dir)
for i in range(len(files)):
    filename = os.fsdecode(files[i])
    img = cv2.imread(dir_in_string + filename)
    out_path = dir_out_string + str(indices[i]) + "/" + filename
    if not os.path.exists(out_path):
        cv2.imwrite(out_path, img)
    print(out_path)


