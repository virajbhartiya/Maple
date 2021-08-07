import numpy as np
import os
import pandas as pd
import requests
from printing import close
import sys
import ctypes

def dbMaker(path):
    # image_dir = filedialog.askdirectory()
    image_dir = path
    # filep = os.path.realpath(__file__)
    # image_dir = os.path.dirname(filep)+"\student_db"

    # photo formats
    formats = ['.ai', '.bmp', '.jpg', '.jpeg', '.png',
               '.ps', '.psd', '.svg', '.tif', '.tiff', 'cr2']

    data = []
    names = []
    rolls = []
    for _, filename in enumerate(os.listdir(image_dir), start=1):
        if filename[filename.index('.'):] in formats:
            new_name = filename.replace(" ", "_")
            roll = new_name[new_name.rindex('_')+1:new_name.rindex('.')]
            os.rename(str(image_dir) + os.sep + filename,
                      str(image_dir)+os.sep + new_name)
            data.append([new_name[:new_name.rindex('_')].replace(
                '_', ' ').capitalize(), new_name, roll])
            
            names.append(new_name[:new_name.rindex('_')].replace(
                '_', ' ').capitalize())
            rolls.append(roll)
    
    createSheet(names, rolls)

    df = pd.DataFrame(data, columns=['Name', 'Image', 'Roll No'])
    df.to_excel(path+"/people_db.xlsx")

    df = xl = pd.ExcelFile(path+"/people_db.xlsx")
    df = xl.parse("Sheet1")
    df = df.sort_values(by='Name')

    writer = pd.ExcelWriter(path+'/output.xlsx')
    df.to_excel(writer, sheet_name='Sheet1', columns=[
                "Name", "Image", "Roll No"], index=False)
    writer.save()
#    ctypes.windll.kernel32.SetFileAttributesW('F:\Maple\Cloud\student_db\people_db.xlsx', 2)


def createSheet(names, roll):
    seperator = ","
    seperator.join(names)
    seperator.join(roll)
    update = requests.get(
        f'https://script.google.com/macros/s/AKfycbx6QqeHusypbgbQclo39C_XsN7OfS0Jqv6nYEnEO3SfWWPQ68LevrnSVARHoJosHJ9ZZw/exec?key=create&names={names}&roll={roll}').text
        
    if update == 'Fail':
        close()
        os._exit(1)
 
