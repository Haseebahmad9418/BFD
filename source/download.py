import requests
import json
import os
import shutil
def download(): 
    file = open("path.txt", "r")
    directoryPath = file.read()
    print(directoryPath)
#     
    Delete = (directoryPath + "/data")
    
    shutil.rmtree(Delete)


    
    os.mkdir(directoryPath + "/data")
    os.mkdir(directoryPath + "/data/Thumbnails")
    os.mkdir(directoryPath + "/data/Content")

    print("Starting download.")
    credfile= directoryPath + "/source/credentials.txt"

    file1 = open(credfile, "r")
    for line in file1:
        feilds=line.split(".")
        ckey=feilds[0]
        kkey=feilds[1]
        file1.close
    res = requests.get("http://bigfatdisplays.com/bigfatdisplays/?ClientKey="+ckey+"&KioskKey="+kkey)
    data = json.loads(res.text)
    print(data)
    http = "http://bigfatdisplays.com/"
    for entry in data:
        print("Downloading thumbnail: " +entry['CONTENTTHUMBNAIL'])
        thumbnailWeb = entry['CONTENTTHUMBNAIL']
        thumbnail_path = directoryPath + '/data/Thumbnails/'
        thumbnail_ext = os.path.splitext(thumbnailWeb)[1]
        #print("Thumbnail ext: " + thumbnail_ext)
        if not os.path.isdir(thumbnail_path):
            os.makedirs(thumbnail_path)
        f = http + thumbnailWeb
        req = requests.get(f)
        with open(thumbnail_path + entry['CONTENTUUID'] + thumbnail_ext , 'wb') as file:
            file.write(req.content)
        print("Downloading content: " + entry['CONTENTITEM'])
        contentWeb = entry['CONTENTITEM']
        content_path = directoryPath + '/data/Content/'
        content_ext = os.path.splitext(contentWeb)[1]
        #print("Content ext: " + content_ext)
        if not os.path.isdir(content_path):   
            os.makedirs(content_path)
        g = http + contentWeb 
        req = requests.get(g)
        with open(content_path + entry['CONTENTUUID'] + content_ext , 'wb') as file:
            file.write(req.content)
    print("Download completed successfully.")
