from skimage.io import imread
from skimage.filter import threshold_otsu
from skimage.measure import label


def otsu_labeling(image):
    image = image > threshold_ostu(image)
    return label(image)


