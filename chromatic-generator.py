# chromatic-generator.py
import glob, os, argparse, shutil
from PIL import Image

# Decode command line arguments
parser = argparse.ArgumentParser(description='Creates beautiful HTML photo galleries with the help of chromatic.js')

parser.add_argument('inputdir', help='Source directory with the images')
parser.add_argument('outputdir', help='Target directory for the gallery files')
parser.add_argument('-f', '--force', action='store_true', help='Overwrite files in target directory')

parser.add_argument('-tw', '--thumbwidth', help='Maximum width of the thumbnails', default=800)
parser.add_argument('-th', '--thumbheight', help='Maximum height of the thumbnails', default=800)

args = parser.parse_args()

# Validate inputs
inputdir = os.path.abspath(args.inputdir)
outputdir = os.path.abspath(args.outputdir)

if inputdir == outputdir:
    raise ValueError('Source and target directory cannot be identical')

thumbnailsize = args.thumbwidth, args.thumbheight

# Prepare target directories
if not os.path.isdir(outputdir):
    os.makedirs(outputdir)

os.makedirs(outputdir + '/images')
os.makedirs(outputdir + '/thumbnails')
os.makedirs(outputdir + '/chromatic')

# Prepare gallery files
chromaticdir = os.path.dirname(os.path.abspath(__file__)) + '/chromatic.js'
shutil.copy2(chromaticdir + '/dist/chromatic.js', outputdir + '/chromatic/chromatic.js')
shutil.copy2(chromaticdir + '/lib/jquery-2.1.1.min.js', outputdir + '/chromatic/jquery.js')
shutil.copy2(chromaticdir + '/stylesheets/chromatic.css', outputdir + '/chromatic/chromatic.css')

# Find all images
sourceImages = glob.glob(inputdir + '/*.jpg')

for sourceImage in sourceImages:
    filename = os.path.basename(sourceImage)

    # Copy images
    shutil.copy2(sourceImage, outputdir + '/images/' + filename)

    # Create thumbnails

    # TODO

    # Store information and aspect ratio

# Create index.html

# TODO

