# chromatic-generator.py
import glob, os, argparse
from PIL import Image

# Decode command line arguments
parser = argparse.ArgumentParser(description='Prepares images and creates a JSON file for consumption with chromatic.js')

parser.add_argument('inputdir', help='Source directory with the images')
parser.add_argument('outputdir', help='Target directory for resized images, thumbnails and JSON file')
parser.add_argument('--urlprefix', help='Prefix added to the filename in the JSON file', default='')
parser.add_argument('-f', '--force', help='Overwrite image files in target directory')

parser.add_argument('--width', help='Maximum width of resized images')
parser.add_argument('--height', help='Maximum height of resized images')

args = parser.parse_args()

if args.inputdir == args.outputdir:
    raise ValueError('Source and target directory can not be identical')

# Copy images

# TODO

# Create thumbnails

# TODO

# Create JSON

# TODO

