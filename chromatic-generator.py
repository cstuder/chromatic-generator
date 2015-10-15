# chromatic-generator.py
import glob, os, argparse, shutil, json
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
    raise ValueError('Source and target directory cannot be identical.')

thumbnailsize = args.thumbwidth, args.thumbheight

# Prepare target directories
if not os.path.isdir(outputdir):
    os.makedirs(outputdir)
elif not args.force:
    raise FileExistsError('Target directory already exists. Use --force to overwrite.')

dirs = ['/images', '/thumbnails', '/chromatic']

for dir in dirs:
    if not os.path.isdir(outputdir + dir):
        os.makedirs(outputdir + dir)

# Prepare gallery files
files = ['/dist/chromatic.js', '/lib/jquery-2.1.1.min.js', '/stylesheets/chromatic.css']
chromaticdir = os.path.dirname(os.path.abspath(__file__)) + '/chromatic.js'

for file in files:
    shutil.copy2(chromaticdir + file, outputdir + '/chromatic/' + os.path.basename(file))

# Find all images
photoList = []
sourceImages = glob.glob(inputdir + '/*.jpg')

for sourceImage in sourceImages:
    filename = os.path.basename(sourceImage)

    # Copy images
    shutil.copy2(sourceImage, outputdir + '/images/' + filename)

    # Create thumbnails
    image = Image.open(sourceImage)
    aspectRatio = image.width / image.height
    image.thumbnail(thumbnailsize)
    image.save(outputdir + '/thumbnails/' + filename)
    image.close()

    # Store information and aspect ratio
    photoList.append({
        'big': 'images/' + filename,
        'small': 'thumbnails/' + filename,
        'aspect_ratio': aspectRatio
    })

# Create index.html
with open(os.path.dirname(os.path.abspath(__file__)) + '/templates/index.html', 'r') as indexFile:
    index = indexFile.read()

with open(outputdir + '/index.html', 'w') as newIndexFile:
    newIndexFile.write(index.replace('CHROMATICGALLERYDEFINITION', json.dumps(photoList), 1))
