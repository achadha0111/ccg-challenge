from utils import LoadRawImageData

unzipped = LoadRawImageData.uncompressFile("data_pipeline/train-images-idx3-ubyte.gz")

images = LoadRawImageData.extractRawData(unzipped)

LoadRawImageData.writeDataToFile(images)


