#! python3
from __future__ import print_function
import sys
import os
import shutil
import zipfile
from PIL import Image
import json


def main():
    print('Started...')

    zipPath = sys.argv[1]

    check_zipfile(zipPath)

    print('Done.')


def check_zipfile(zipPath):

    if(os.path.exists(zipPath) and zipPath.endswith('.zip')):
        run_program(zipPath)
    elif (os.path.exists(zipPath) == False):
        print("Invalid file Path")



def run_program(zipPath):
    temporaryFile = os.path.join(os.getcwd(), 'TempFile\\')

    create_tempFile(temporaryFile)

    data = unzip_file(zipPath, temporaryFile)

    create_directory_structure(data, temporaryFile)

    remove_tempFile_items(data, temporaryFile)

    make_zipfile(temporaryFile)

    os.chdir(temporaryFile)

    delete_tempFile(temporaryFile)





def unzip_file(zipPath, temporaryFile):
    with zipfile.ZipFile(zipPath) as myZip:
        myZip.extractall(temporaryFile)

        with open('TempFile\\manifest.json') as data_file:
            data = json.load(data_file)

        myZip.close()
    return data


def remove_tempFile_items(data, temporaryFile):
    for i in data['zip_contents']:
        os.remove(temporaryFile + i)

    os.remove(temporaryFile + 'manifest.json')


def make_thumbnails(image, temporaryFile, folder_path):
    size = (100, 100)
    im = Image.open(temporaryFile+image)
    im.thumbnail(size)
    im.save(os.path.splitext(folder_path+image)[0] +'_thumbnail.jpg')


def make_zipfile(temporaryFile):
    shutil.make_archive(temporaryFile, 'zip', temporaryFile)


def create_tempFile(temporaryFile):
    try:
        os.mkdir(temporaryFile)
    except:
        print('{} folder is already created'.format(temporaryFile))

def delete_tempFile(temporaryFile):
    os.chdir(os.path.dirname(os.path.dirname(temporaryFile)))
    shutil.rmtree('TempFile')


def create_directory_structure(data, temporaryFile):
    for key in data.keys():
        if (key == 'directory_structure'):
            for image_themes in data[key]:
                if (image_themes.endswith('.jpg') or image_themes.endswith('.jpeg')):
                    create_images_in_file(temporaryFile, temporaryFile, folder)
                else:
                    create_image_folder(temporaryFile, image_themes)
                    image_themes_path = create_path_name(temporaryFile, image_themes)

                for folder in data[key][image_themes]:
                    if (folder.endswith('.jpg') or folder.endswith('.jpeg')):
                        create_images_in_file(image_themes_path, temporaryFile, folder)
                    else:
                        create_image_folder(image_themes_path, folder)
                        folder_path = create_path_name(image_themes_path, folder)

                    for image in data[key][image_themes][folder]:
                        if (image.endswith('.jpg') or image.endswith('.jpeg')):
                            create_images_in_file(folder_path, temporaryFile, image)
                        else:
                            create_image_folder(folder_path, image)
                            new_folder_path = create_path_name(folder_path, image)

                            for nextImage in data[key][image_themes][folder][image]:
                                create_images_in_file(new_folder_path, temporaryFile, nextImage)



def create_images_in_file(folder_path, temporaryFile, image):
    os.chdir(folder_path)
    shutil.copy(temporaryFile + image, folder_path)
    make_thumbnails(image, temporaryFile, folder_path)


def create_image_folder(file_location, file):
    try:
        os.mkdir(file_location + file)
    except:
        print('{} folder is already created'.format(file))


def create_path_name(base_path, file_name):
    return base_path + file_name + '\\'

if __name__ == '__main__': main()