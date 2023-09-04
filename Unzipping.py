import os
import gzip
import shutil

# Define the root directory where the patient folders are located
root_dir =  'C:\\Users\\SURUTHI S\\Desktop\\BRATS 2023\\DataSet\\BraTS2023-PED-Challenge-TrainingData\\ASNR-MICCAI-BraTS2023-PED-Challenge-TrainingData\\'


# For the Count
itr = 0 
itr_2 = 0

# Scans all the folders from BraTS-PED-00002-000 to BraTS-PED-00171-000 
for i in os.listdir(root_dir):
    path_pat = os.path.join(root_dir,i)
    itr = itr+1 # returns 99 (as many folders of patients)
    
    
    for nii_images in os.listdir(path_pat):  # for each folder looping through to extract the .nii.gz into .nii files
        file_pat = os.path.join(path_pat, nii_images)  
        output = file_pat[:-3]  # without .gz extension
        with gzip.open(file_pat, 'rb') as gz_file , open(output,'wb') as out_file : # unzipping
           shutil.copyfileobj(gz_file, out_file) 
        itr_2 += 1 # counting the files modififed # 99* 5 = 495 files
        
        os.remove(file_pat) # removing .gz files and retaining only .nii files
    
print(itr)

print('itr_2',itr_2)

