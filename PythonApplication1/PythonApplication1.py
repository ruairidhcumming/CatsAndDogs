
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os
print(os.listdir(".."))

## create image preprocessor
datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

