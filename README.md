# ImageAnnotationTools
Classifier and region selection tools for generating training datasets in python
The example data was downloaded from the dogs vs cats dataset on kaggle: https://www.kaggle.com/datasets/biaiscience/dogs-vs-cats

Binary Image Annotation:
annotate_images.py generates a list of file paths for each class and writes them to excel spreadsheets. When executed, the script will prompt the user to specify two directory paths:
  1) folder_path: the directory path containing the raw image data
  2) output_path: the directory to write excel spreadsheets containing image paths for classification
The program will iteratively cycle through each image in the directory and only proceed with a keypress. To categorize an image into either class, the user must use the 'A' (left directory) or 'D' (right directory) keys. Other keys will be registered; however, those image file paths will NOT be stored.
**Supported file types: '.png', '.jpg', '.jpeg', '.gif', '.bmp'

Manual Image Segmentation:
manual_segmentation.py allows the user to create binary mask files, writing them to the same 
