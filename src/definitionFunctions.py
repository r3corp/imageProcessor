import dhash
from PIL import Image


def imageToProcess(imagePath):
    openedImage = Image.open(imagePath)
    hashRow, hashCol = dhash.dhash_row_col(openedImage)
    return dhash.format_hex(hashRow, hashCol) + " - " + imagePath 
    