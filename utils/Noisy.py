""" Reference -

https://stackoverflow.com/questions/22937589/how-to-add-noise-gaussian-salt-and-pepper-etc-to-image-in-python-with-opencv

"""

import numpy as np
from multiprocessing import Pool
from random import randint


def addGaussianNoise(image):

    row, col = image.shape
    mean = 0
    var = 0.1
    sigma = var**0.5

    gaussian = np.random.normal(mean, sigma, (row, col))

    gaussian = gaussian.reshape(row, col)
    noisyImage = image + gaussian
    return noisyImage


def addPoissonNoise(image):

    vals = len(np.unique(image))
    vals = 2 ** np.ceil(np.log2(vals))
    noisy = np.random.poisson(image * vals) / float(vals)
    return noisy

def createNoisyImage(imageData, numProcesses):

    noiseToUse = "gaussian" if randint(1, 2) == 1 else "poisson"

    # TODO Pool doesn't preserve order, images written to disk would not be linked
    with Pool(numProcesses) as p:
        # Not entirely happy with this block of code, alas, lambda functions aren't pickleable
        if noiseToUse == "gaussian":
            noisyImages = p.map(addGaussianNoise, imageData)
        else:
            noisyImages = p.map(addPoissonNoise, imageData)

    return noisyImages