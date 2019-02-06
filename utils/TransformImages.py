import cv2
import numpy as np
from multiprocessing import Pool
from .DiskWriteUtil import writeDataToFile


def rotateImage(image):
    image = image.astype(np.uint8)
    rows, cols = image.shape

    rotationAngle = getRandomTransformationValue(-100, 100, "degree")

    # Rotate pixels
    M = cv2.getRotationMatrix2D((cols/2, rows/2), rotationAngle, 1)
    rotatedImage = cv2.warpAffine(image, M, (cols, rows))

    return rotatedImage


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


def getRandomTransformationValue(start, end, unit):
    if unit == "degree":
        return np.random.uniform(start, end+1)
    elif unit == "%":
        return (1/100)*np.random.uniform(start, end+1)


def applyTransformations(imageData, numProcesses):
    # combinedTransformation = composeTransformations(rotateImage, translateImage)

    with Pool(numProcesses) as p:
        # Not entirely happy with this block of code, alas, lambda functions aren't pickleable
        translatedImages = p.map(translateImage, imageData)
        transformedImages = p.map(rotateImage, translatedImages)

    return transformedImages


