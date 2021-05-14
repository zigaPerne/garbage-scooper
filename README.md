# Garbage Scooper

Console script for downloading images from 4chan. The script scrapes the given thread for all image and video files (jpg, png, gif, webm) and saves them to a specified folder.

Requires python3.

## Install and run

Download:

    git clone https://github.com/zigaPerne/garbage-scooper
    cd garbage scooper
Run:

    python3 garbage-scooper.py
    
The program then asks you for a thread URL and the directory path. Simply paste these values into the console.

## Flags

    usage: 4chDL.py [-h] [-w WAIT] [-wms WAIT_MILISECONDS] [-i INCLUDE] [-e EXCLUDE]
                    [-d DUPLICATE]

    optional arguments:
      -h, --help            show this help message and exit
      -w WAIT, --wait WAIT  Specify time between downloading images in s
      -wms WAIT_MILISECONDS, --wait-miliseconds WAIT_MILISECONDS
                            Specify time between downloading images in ms
      -i INCLUDE, --include INCLUDE
                            Download ONLY specified filetype. Include multiple
                            filetypes separated with commas in quotes. (ex: -i "jpg,
                            gif")
      -e EXCLUDE, --exclude EXCLUDE
                            Download all filetypes except specified. Include
                            multiple filetypes separated with commas in quotes. (ex:
                            -e "jpg, gif")
      -d DUPLICATE, --duplicate DUPLICATE
                            Check if image filename already exists in the directory.
                            If yes, the image will not be downloaded. If no, file
                            will be replaced. Values: 1 = check; 0 = don't check;
                            Default = 1

