# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from skimage.io import iread

from skimage.filter import threshold_otsu
from skimage.measure import label
def otsu_labeling(image):
    image = image > threshold_otsu(image)
    return label(image)
