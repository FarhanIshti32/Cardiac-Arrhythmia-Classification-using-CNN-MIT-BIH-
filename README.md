# Cardiac-Arrhythmia-Classification-using-CNN-MIT-BIH-
1. Download the MIT-BIH dataset.
2. Use the all_csv_to_one_csv.py to create a csv file that contains all the patient data together. You should do this for each class separately. So you will have a csv of ecg data for each class.
3. Use the csv_to_image.py to convert the continuous time-series ecg data to 64x64 images of each heart beat using peek detection.
4. Finally use the VGG_Arr.ipynb file to run the classification
