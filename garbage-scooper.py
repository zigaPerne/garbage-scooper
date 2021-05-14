from requests import get
import urllib.request
from time import sleep
from bs4 import BeautifulSoup
from flags import *


# Makes crude array of strings containing image url (and other junk):
def prepareDL(url):
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

# Checks filetype (for flags -i and -e)
def check_filetype(filetype, include_exclude):
    if include_exclude[-1] == "i":
        for i in include_exclude[0]:
            if filetype[1:] == i: return 0
        return 1
    else:
        for i in include_exclude[0]:
            if filetype[1:] == i: return 1
        return 0 

# Checks if filename is duplicate:
def check_folder(check, imgname):
    if check == 0: 
        return 1

    try:
        f = open(imgname)
        f.close()
        return 0
    except:
        return 1      

# URL and path prep and download
def download(url, path, time, check, include_exclude):
    https = "https:"
    path_slash = "/"
#   path_slash = "\\"
    images = prepareDL(url)

    for i in images[::2]:
        slash = i.find("//")
        quote = i.find("\"", slash)
        link = https + i[slash:quote]
        dot = link.find(".", len(link) - 10)
        filetype = link[dot:]
        if include_exclude and check_filetype(filetype, include_exclude):
            continue
        name_start = (i.find("1"))
        name_end = (i.find(".", name_start))
        name = i[name_start:name_end]
        filepath = path + path_slash + name + filetype
        if check_folder(check, filepath):
            urllib.request.urlretrieve(link, filepath)
            sleep(time)
    print("Done")    

# Check flags:
args = parse()
wait = args.wait
wait_miliseconds = args.wait_miliseconds
include = args.include
exclude = args.exclude
duplicate = args.duplicate

if (wait and wait_miliseconds) or (exclude and include):
    print("Flags in conflict!")
    exit()

if wait: time = wait
elif wait_miliseconds: time = wait_miliseconds / 100
else: time = 0

if include: i_e = [include.split(", "), "i"]
elif exclude: i_e = [exclude.split(", "), "e"]
else: i_e = 0

url = input("Thread url: ")
path = input("Directory to save files: ")
download(url, path, time, duplicate, i_e)

