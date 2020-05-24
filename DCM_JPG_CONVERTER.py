#DCM FILE to JPG Image converter 
#Written on 24 May 2020 
# Author: Hithesh Karanth 
import pydicom as dicom
import matplotlib.pyplot as plt
import matplotlib.image as images
import os
import numpy as np
import cv2
import scipy.ndimage as ndimage

#Set this for getting more contrast higher value means more contrast
Threshold = 6.0

#Add dcm path and string path over here 
dcm_folder_path = "C:/Users/HITHESH KARANTH/Desktop/DATA CT SCAN/TCGA-OV/TCGA-09-0369/04-10-1995-CT ABD PELV EN-76404/2.000000-5MM HELICAL-35189"
jpg_file_path = "C:/Users/HITHESH KARANTH/Desktop/DATA CT SCAN/DICOM-to-JPG-master/Output_2/"

copies_transfered =0
images_path = os.listdir(dcm_folder_path)

for n, image in enumerate(images_path):
        copies_transfered=copies_transfered+1
        print(copies_transfered)
        ds = dicom.dcmread(os.path.join(dcm_folder_path, image))
        if 'WindowWidth' in ds:
            print('Dataset has windowing')

        windowed = dicom.pixel_data_handlers.util.apply_modality_lut(ds.pixel_array, ds)
        # Rescaling grey scale between 0-255
        image_2d_scaled = (np.maximum(windowed,0) / windowed.max()) * 255.0

        # Convert to uint
        image_2d_scaled = np.uint8(image_2d_scaled)
        # Contrast setting CLAHE mechanism
        clahe = cv2.createCLAHE(clipLimit=Threshold, tileGridSize=(6,6))
        image_2d_scaled = clahe.apply(image_2d_scaled)
        
        #Saving output from the DCM to jpg
        Final_Folder_path = jpg_file_path + image.replace('.dcm', '.jpg')
        images.imsave(Final_Folder_path, image_2d_scaled , cmap='gray', vmin=0, vmax=255)

