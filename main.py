from utils import LoadRawImageData, DiskWriteUtil, TransformImages

unzipped = LoadRawImageData.uncompressFile("data_pipeline/train-images-idx3-ubyte.gz")

images = LoadRawImageData.extractRawData(unzipped)

DiskWriteUtil.writeDataToFile(images, "rawImages", "raw")

transformedImages = TransformImages.applyTransformations(images, 2)

DiskWriteUtil.writeDataToFile(transformedImages, "transformedImages", "transformed")


