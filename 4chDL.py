from requests import get
import urllib.request
from time import sleep
from bs4 import BeautifulSoup

def prepareDL(url, path):
    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    lines = soup.findAll("a")
    strlines = []
    for i in lines:
        strlines.append(str(i))
    images = []
    for i in strlines:
        if "//i.4cdn.org" in i:
            images.append(i)
    return images

def checkfolder(imgname):
    try:
        f = open(imgname)
        f.close()
        return 0
    except:
        return 1      

def download(url, path):
    https = "https:"
    backslash = "\\"
    images = prepareDL(url, path)
    
    for i in images[::2]:
        slash = i.find("//")
        quote = i.find("\"", slash)
        link = https + i[slash:quote]
        dot = link.find(".", len(link) - 10)
        name_start = (i.find("1"))
        name_end = (i.find(".", name_start))
        name = i[name_start:name_end]
        filetype = link[dot:]
        filepath = path + "/" + name + filetype
        if checkfolder(filepath):
            urllib.request.urlretrieve(link, filepath)
            sleep(1)
    print("Done")    

url = input("url: ")
path = input("path: ")
download(url, path)

