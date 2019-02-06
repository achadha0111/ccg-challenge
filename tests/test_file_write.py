import unittest
import utils.DiskWriteUtil as writeImage
from os import path, walk
from cv2 import imread
import shutil

# DONE COMPLETE TESTING


class DataExtractionTests(unittest.TestCase):

    def setUp(self):
        self.mockImagePath = "testImgs/test.png"
        self.directoryPath = "mockDirectory"
        self.description = "imageDescription"

    # Test creating a specified folder and writing a PNG file to it
    def testDiskWrite(self):
        # Get image into a numpy array
        im = imread(self.mockImagePath)
        # Write image to disk
        writeImage.writeDataToFile(im, self.directoryPath, self.description)
        # Verify directory created
        self.assertTrue(path.exists(self.directoryPath))
        for (dirpath, dirname, files) in walk(self.directoryPath):
            # Verify file added with an index, given description and extension PNG
            for file in files:
                filename, file_extension = file.split(".")
                self.assertIn("imageDescription", filename)
                self.assertEqual("png", file_extension)

    def tearDown(self):
        shutil.rmtree(self.directoryPath)







