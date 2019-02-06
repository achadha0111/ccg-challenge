from os import path, makedirs
import imageio

"""
Writes the images to disk

Args:
    imageData: A numpy array containing the images and their pixel values.
    directory: The directory that must be created to store the images.
    description: A string value to describe the saved images

Returns:
    None

"""

def writeDataToFile(imageData, directory, description):

    if not path.exists(directory):
        makedirs(directory)

    # TODO Optimise this (?)

    for idx, file in enumerate(imageData):
        fileName = "{0}_{1}.png".format(description, idx)
        imageio.imwrite(path.join(directory, fileName), file)