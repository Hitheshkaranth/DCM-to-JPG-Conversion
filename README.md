# DCM-to-JPG-Conversion
I was finding it bit difficult to convert a batch of DCM file to jpg file for making training data sets so I put together this code.

The output images are still bit noisy.

Requirement:
OpenCV for python 
matplotlib
numpy
scipy
pydicom


Useage:

before running the code make sure to edit:
dcm_folder_path = "PATH_OF_DCM_FILES"

jpg_file_path = "PATH_TO_STORE_JPG"

dcm_folder_path is the folder path containing .dcm file 
jpg_file_path is the path for saving .jpg file converted from .dcm
