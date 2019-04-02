import os
import cv2
import numpy as np
import nibabel as nib

def resizeAndSaveNifty(path, size, inter):
    size = 128
    new_size_y = 128
    initial_image = nib.load(path).get_data()
    slices = initial_image.shape[2]
    new_data = np.zeros((size,new_size_y,slices))

    for i in range(0,slices):
        temp_slice = cv2.resize(initial_image[..., i], (size, new_size_y), interpolation=inter)
        new_data[...,i] = temp_slice

    return nib.Nifti1Image(new_data, np.eye(4))

def resizeNiftyFolder(folder, size=128, inter=cv2.INTER_CUBIC):
    if not os.path.exists('resized/'+folder): os.makedirs('resized/'+folder)
    for filename in os.listdir(folder):
        img = resizeAndSaveNifty(folder+filename, size, inter)
        print(folder+filename);
        img.to_filename('resized/'+folder+filename)
