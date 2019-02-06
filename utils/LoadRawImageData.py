import gzip
import numpy as np
import struct as st

'''
:input File path to the compressed file
:returns Unzipped file

'''

"""
Decompresses file using gunzip

Args:
    filepath: File path to the compressed file

Returns:
   Reference to the file
   
"""


def uncompressFile(filepath):
    f = gzip.open(filepath, 'rb')
    return f


"""
Extracts Raw Data

Args:
    uncompressedFile: File path to the uncompressed file

Returns:
   Uncompressed Image Data
   
Taken from - https://medium.com/@mannasiladittya/converting-mnist-data-in-idx-format-to-python-numpy-array-5cb9126f99f1

"""


def extractRawData(uncompressedFile):

    imagefile = uncompressedFile
    imagefile.seek(0)

    seed = st.unpack('>4B', imagefile.read(4))
    numImages = st.unpack('>I', imagefile.read(4))[0]
    numRows = st.unpack('>I', imagefile.read(4))[0]
    numColumns = st.unpack('>I', imagefile.read(4))[0]

    totalBytes = numImages*numRows*numColumns

    imageArray = 255 - np.asarray(st.unpack('>'+'B'*totalBytes, imagefile.read(totalBytes))).reshape((
        numImages, numRows, numColumns))

    return imageArray


