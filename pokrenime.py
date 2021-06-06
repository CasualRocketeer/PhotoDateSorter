from PIL import Image
import os
import shutil
import exifread
def get_date(path):
    return Image.open(path).getexif()[36867][:4]

image_folder_path=os.getcwd()

for im in os.listdir(image_folder_path):
    image_path = os.path.join(image_folder_path, im)
    if image_path[-4:]==".jpg":
        image_date=get_date(image_path)
        #napravi folder ako ne (jer bi se neki datumi slika mogli ponavljati)
        if image_date not in os.listdir(image_folder_path):
            date_folder_path=os.path.join(image_folder_path,image_date)
            os.mkdir(date_folder_path)
            shutil.move(image_path,date_folder_path)
        else:
            date_folder_path = os.path.join(image_folder_path, image_date)
            shutil.move(image_path, date_folder_path)
    else:
        pass
