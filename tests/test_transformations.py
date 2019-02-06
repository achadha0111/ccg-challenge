import unittest
import utils.TransformImages as transform
from os import path, walk
from cv2 import imread
import numpy as np

# DONE COMPLETE TESTING


class TransformationTests(unittest.TestCase):

    def setUp(self):
        self.mockImagePath = "testImgs/test.png"

    # Test whether the translated image array is different from the original one
    # We don't test the affine transformations themselves on the assumption that openCV tests it
    def testTranslation(self):
        # Get image into a numpy array
        im = imread(self.mockImagePath, 0)
        transformedImage = transform.translateImage(im)
        self.assertFalse(np.array_equal(im, transformedImage))

    def testRotation(self):
        im = imread(self.mockImagePath, 0)
        transformedImage = transform.rotateImage(im)
        self.assertFalse(np.array_equal(im, transformedImage))

    # Should return a number between -100 and 100 for the argument degrees
    def testGetUniformRandomNumberWithDegree(self):
        randomUniformRotationValue = transform.getRandomTransformationValue(-100, 100, "degree")
        self.assertLessEqual(randomUniformRotationValue, 100)
        self.assertGreaterEqual(randomUniformRotationValue, -100)

    # Should return a percentage
    def testGetUniformRandomNumberWithPercentage(self):
        randomUniformTranslationValue = transform.getRandomTransformationValue(-40, 40, "%")
        self.assertLessEqual(randomUniformTranslationValue, 0.4)
        self.assertGreaterEqual(randomUniformTranslationValue, -0.4)