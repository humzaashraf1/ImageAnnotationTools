# ImageAnnotationTools
Classifier and region selection tools for generating training datasets in python
The example data was downloaded from the dogs vs cats dataset on kaggle: https://www.kaggle.com/datasets/biaiscience/dogs-vs-cats

Binary Image Annotation:
annotate_images.py generates a list of file paths for each class and writes them to excel spreadsheets. When executed, the script will prompt the user to specify two directory paths:
  1) folder_path: the directory path containing the raw image data
  2) output_path: the directory to write excel spreadsheets containing image paths for classification

The program will iteratively cycle through each image in the directory and only proceed with a keypress. To categorize an image into either class, the user must use the 'A' (left directory) or 'D' (right directory) keys. Other keys will be registered; however, those image file paths will NOT be stored.
**Supported file types: '.png', '.jpg', '.jpeg', '.gif', '.bmp'

![image](https://github.com/humzaashraf1/ImageAnnotationTools/assets/121640997/ebf02b68-625c-4a35-a15e-64f850716a83)

Manual Image Segmentation:
manual_segmentation.py allows the user to create binary mask files from a folder of images. The masks are written to a new folder with the same file name and in the same format. When executed, the script will prompt the user to specify two directory paths:
  1) input_folder: the directory containing the raw image data
  2) output_folder: the directory to write mask files

The CV2 polygon drawer tool will allow the user to create a mask by holding down the left mouse button and free-handing an enclosed polygon. Hit 'Enter' to proceed to the next image.
**Supported file types: '.png', '.jpg', '.jpeg', '.gif', '.bmp'

![cat 2956](https://github.com/humzaashraf1/ImageAnnotationTools/assets/121640997/a7d44628-73f3-4e3d-a7d4-efa73db25944)
![cat 2956](https://github.com/humzaashraf1/ImageAnnotationTools/assets/121640997/12699377-e683-4af5-af2d-ac8b62757519)

**Portions of code in this repository were generated with the assistance of ChatGPT, an AI language model developed by OpenAI.**
