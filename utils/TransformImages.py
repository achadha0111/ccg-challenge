import cv2
import numpy as np
from multiprocessing import Pool

"""
Rotate Image

Args:
    image: A numpy array representation of the image

Returns:
   Image rotated by an angle between -100 to 100 degree (sampled from a uniform distribution) with respect to the center.

"""
def rotateImage(image):
    image = image.astype(np.uint8)
    rows, cols = image.shape

    rotationAngle = getRandomTransformationValue(-100, 100, "degree")

    # Rotate pixels
    M = cv2.getRotationMatrix2D((cols/2, rows/2), rotationAngle, 1)
    rotatedImage = cv2.warpAffine(image, M, (cols, rows))

    return rotatedImage


"""
Translate Image

Args:
    image: A numpy array representation of the image

Returns:
   Image translated along both the axes by a percentage between -40 to 40 degree (sampled from a uniform distribution)

"""


def translateImage(image):
    image = image.astype(np.uint8)
    rows, cols = image.shape

    # Get translation values
    xTranslation = getRandomTransformationValue(-40, 40, "%")*cols
    yTranslation = getRandomTransformationValue(-40, 40, "%")*rows

    # Apply transformation
    M = np.float32([[1, 0, xTranslation], [0, 1, yTranslation]])
    translatedImage = cv2.warpAffine(image, M, (cols, rows))

    return translatedImage


"""
Return random transformation value to use

Args:
    start: start of range
    end: end of range
    unit: "%" or "degree" to differentiate between rotation and translation

Returns:
   A value (scaled appropriately) for carrying out the transformation

"""


def getRandomTransformationValue(start, end, unit):
    if unit == "degree":
        return np.random.uniform(start, end+1)
    elif unit == "%":
        return (1/100)*np.random.uniform(start, end+1)


"""
Applies transformations to a numpy array of images

Args:
    imageData: Numpy array containing images
    numProcesses: Processes to use for concurrent execution

Returns:
   A numpy array containing transformed images

"""


def applyTransformations(imageData, numProcesses):
    # combinedTransformation = composeTransformations(rotateImage, translateImage)

    # TODO Pool doesn't preserve order, images written to disk would not be linked
    with Pool(numProcesses) as p:
        # Not entirely happy with this block of code, alas, lambda functions aren't pickleable
        translatedImages = p.map(translateImage, imageData)
        transformedImages = p.map(rotateImage, translatedImages)

    return transformedImages


