from utils import LoadRawImageData, DiskWriteUtil, TransformImages, Noisy
import argparse
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# DONE Add argparser to allow command line execution
parser = argparse.ArgumentParser()

parser.add_argument("--processes", default=2, help="Specify number of processes to use for image processing")

parser.add_argument("--verbose", action="store_true", help="Output pipeline status to standard output")

# TODO setup argument parsing to allow provision of paths instead of having them hardcoded
# parser.add_argument("--images")

args = parser.parse_args()


def main():

    logger.info("Uncompressing file")
    unzipped = LoadRawImageData.uncompressFile("data_pipeline/train-images-idx3-ubyte.gz")

    logger.info("Extracting raw data")
    images = LoadRawImageData.extractRawData(unzipped)

    logger.info("Applying transformations")
    transformedImages = TransformImages.applyTransformations(images, int(args.processes))

    logger.info("Writing transformed images to the directory transformedImages")
    DiskWriteUtil.writeDataToFile(transformedImages, "transformedImages", "transformed")

    logger.info("Adding noise to images")
    noisyImages = Noisy.createNoisyImage(transformedImages, int(args.processes))

    logger.info("Saving noisy images to the directory noisyImages")
    DiskWriteUtil.writeDataToFile(noisyImages, "noisyImages", "transformedNoisy")

    logger.info("Images saved. Goodbye!")

if __name__ == "__main__":
    main()
