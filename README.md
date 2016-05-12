# PracticePython
Python practice assignments  

## Project Descriptions
### PictureSorter.py

This project takes a zipped file that contains images and a JSON file. It then creates thumbnails of the images and saves the images in a directory structure that is specified by the JSON file. 

The steps that the program takes are:
* Unzips the images.
* Create thumbnails of the images.
* Put the images (thumbnail and full-size) into the folder structure dictated by the JSON file.
* Zip the resulting directory structure.

The script uses relative paths to move around the directory. 


#####How to run

  * Open command prompt
  * **cd** to the folder that contains **PictureSorter.py**
  * Type **python PictureSorter.py [ZIP FILE LOCATION]** into your command prompt
  
  *Note:* **[ZIP FILE LOCATION]** refers to the file path were you saved your picture zip file. Ex: C:\User\Documents 
