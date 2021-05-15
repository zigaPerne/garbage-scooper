import argparse

def parse():
	parser = argparse.ArgumentParser()
	
	parser.add_argument("-w", "--wait", dest = "wait", help = "Specify time between downloading images in s", type = float)
	parser.add_argument("-wms", "--wait-miliseconds", dest = "wait_miliseconds",  help = "Specify time between downloading images in ms", type = float)
	parser.add_argument("-i", "--include", dest = "include", help = "Download ONLY specified filetype. Include multiple filetypes separated with commas in quotes. (ex: -i \"jpg, gif\")")
	parser.add_argument("-e", "--exclude", dest = "exclude", help = "Download all filetypes except specified. Include multiple filetypes separated with commas in quotes. (ex: -e \"jpg, gif\")")
	parser.add_argument("-d", "--duplicate", dest = "duplicate", default = 1, help = "Check if image filename already exists in the directory and skip download. Values: 1 = check; 0 = don't check (replaces file); Default = 1", type = int)

	return(parser.parse_args())
