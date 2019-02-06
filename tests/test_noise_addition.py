import unittest
import utils.Noisy as makeNoisy
import cv2
import numpy as np

# DONE COMPLETE TESTING


class NoiseAdditionTests(unittest.TestCase):

    def setUp(self):
        self.mockImagePath = "testImgs/test.png"

    def addGaussianNoise(self):
        im = cv2.imread(self.mockImagePath, 0)
        noisyImage = makeNoisy.addGaussianNoise(im)
        self.assertFalse(np.array_equal(im, noisyImage))

    def addPoissonNoise(self):
        im = cv2.imread(self.mockImagePath, 0)
        noisyImage = makeNoisy.addPoissonNoise(im)
        self.assertFalse(np.array_equal(im, noisyImage))


