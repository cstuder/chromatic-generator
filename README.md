# chromatic-generator

Status: Working

A Python 3 command line tool to create beautiful static HTML photo galleries with the help of `chromatic.js`

`chromatic-generator` is ISC licensed and was created by Christian Studer (cstuder@existenz.ch, Bureau für digitale Existenz).

Source: >https://github.com/cstuder/chromatic-generator>

## About chromatic.js

A JavaScript library created by Crispy Mountain which displays beautiful photo galleries. ISC licensed.

Source: <https://github.com/crispymtn/chromatic.js> (Copy included in this repository)

Hosted version: <http://www.chromatic.io> (No longer online)

## Top level usage

1. Collect your images in a directory.
2. Use `chromatic-generator.py` to copy the images, create thumbnails and the gallery files.
3. Open the created index.html in a browser and see your image arranged and displayed in an awesomely beautiful kind of way.

Once created, there are no external dependencies to worry about: All required files (Both images and the gallery scripts itself) are located in the output directory.

## Usage of the command line tool

    python chromatic-generator.py [-h] [-f] [-tw THUMBWIDTH] [-th THUMBHEIGHT]
                              inputdir outputdir

    positional arguments:
      inputdir              Source directory with the images
      outputdir             Target directory for the gallery files

    optional arguments:
      -h, --help            show this help message and exit
      -f, --force           Overwrite files in target directory
      -tw THUMBWIDTH, --thumbwidth THUMBWIDTH
                            Maximum width of the thumbnails (Defaults to 600 pixels)
      -th THUMBHEIGHT, --thumbheight THUMBHEIGHT
                            Maximum height of the thumbnails (Defaults to 600 pixels)

## Status of chromatic-generator

It is Good Enough for my purposes: Creating a gallery from a collection of JPEG files with known-to-be-correct EXIF information.

There will be no more development on my part. (Christian Studer, february 2016)

### Possible improvements for the future

- Other sort orders
- Handling more image file types
- Better error handling
- Multiple galleries
- Prevention of name collisions
