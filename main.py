import os
import cv2
import numpy as np
import nibabel as nib

def resizeAndSaveNifti(path, size=128):
    size = 128
    new_size_y = 128
    initial_image = nib.load(path).get_data()
    slices = initial_image.shape[2]
    new_data = np.zeros((size,new_size_y,slices))
    print(initial_image.shape)

    for i in range(0,slices):
        temp_slice = cv2.resize(initial_image[..., i], (size, new_size_y), interpolation=cv2.INTER_CUBIC)
        new_data[...,i] = temp_slice

    return nib.Nifti1Image(new_data, np.eye(4))

def resizeNiftiFolder(folder):
    if not os.path.exists('resized/'+folder): os.makedirs('resized/'+folder)
    for filename in os.listdir(folder):
        img = resizeAndSave(folder+filename)
        print(folder+filename);
        img.to_filename('resized/'+folder+filename)

resizeNiftiFolder('Task03_Liver/imagesTr/')
