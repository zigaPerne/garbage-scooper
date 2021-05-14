# Garbage scooper
Python script for downloading images from 4chan. Requires python3.



# Flags
usage: 4chDL.py [-h] [-w WAIT] [-wms WAIT\_MILISECONDS] [-i INCLUDE] [-e EXCLUDE]
                [-d DUPLICATE]

optional arguments:
  -h, --help            show this help message and exit
  -w WAIT, --wait WAIT  Specify time between downloading images in s
  -wms WAIT\_MILISECONDS, --wait-miliseconds WAIT\_MILISECONDS
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
