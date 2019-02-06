from os import path, makedirs
import imageio

def writeDataToFile(imageData, directory, description):

    if not path.exists(directory):
        makedirs(directory)

    # TODO Optimise this (?)

    for idx, file in enumerate(imageData):
        fileName = "{0}_{1}.png".format(description, idx)
        imageio.imwrite(path.join(directory, fileName), file)