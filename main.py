from utils import LoadRawImageData, DiskWriteUtil, TransformImages, Noisy

# TODO Add argparser to allow command line execution

unzipped = LoadRawImageData.uncompressFile("data_pipeline/train-images-idx3-ubyte.gz")

images = LoadRawImageData.extractRawData(unzipped)

#DiskWriteUtil.writeDataToFile(images, "rawImages", "raw")

transformedImages = TransformImages.applyTransformations(images, 2)

DiskWriteUtil.writeDataToFile(transformedImages, "transformedImages", "transformed")

noisyImages = Noisy.createNoisyImage(transformedImages, 2)

DiskWriteUtil.writeDataToFile(transformedImages, "noisyImages", "transformedNoisy")


