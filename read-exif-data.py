# Read EXIF data from photo file

import os
from PIL import Image

photoFilePath = 'DSC_0014 (4).JPG'
img = Image.open(photoFilePath)
exif_data = img._getexif()
print(exif_data[36867])