""" Reference -

https://stackoverflow.com/questions/22937589/how-to-add-noise-gaussian-salt-and-pepper-etc-to-image-in-python-with-opencv

"""

import numpy as np
from multiprocessing import Pool
from random import randint

"""
Adds gaussian noise to an image

Args:
    image: A numpy array representation of the image

Returns:
    An image with Gaussian Noise.

"""

def addGaussianNoise(image):

    row, col = image.shape
    mean = 0
    var = 0.1
    sigma = var**0.5

    gaussian = np.random.normal(mean, sigma, (row, col))

    gaussian = gaussian.reshape(row, col)
    noisyImage = image + gaussian
    return noisyImage


"""

Adds noise sampled from a Poisson distribution to an image

Args:
    image: A numpy array representation of the image

Returns:
    An image with Poisson Noise.

"""


def addPoissonNoise(image):

    vals = len(np.unique(image))
    vals = 2 ** np.ceil(np.log2(vals))
    noisy = np.random.poisson(image * vals) / float(vals)
    return noisy


"""

Randomly chooses one of the two noise distributions to use and applies that to the image.
Also maps processes (user specified) to the images to achieve concurrent execution.

Args:
    image: A numpy array representation of the image
    numProcesses: Number of processes to use, default is 2

Returns:
    A numpy array containing images with added noise

"""


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