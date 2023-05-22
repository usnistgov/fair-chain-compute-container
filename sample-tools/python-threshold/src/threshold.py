import argparse
import skimage.io
import numpy as np
from os import listdir
from os.path import isfile, join

def main():
    # Setup CLI Argument parsing
    parser = argparse.ArgumentParser(prog='threshold', description='Create a binary image from a grayscale image and threshold value')

    # Define arguments
    parser.add_argument('--inputImages', dest='input_images', type=str, help='filepath to the directory containing the images', required=True)
    parser.add_argument('--thresholdValue', dest='threshold_value', type=int, required=True)
    parser.add_argument('--output', dest='output_folder', type=str, required=True)

    # Parse arguments
    args = parser.parse_args()
    input_images = args.input_images
    threshold_value = args.threshold_value
    output_folder = args.output_folder

    # Print parsed arguments
    print('*** Arguments:')
    print('inputImages = {}'.format(input_images))
    print('thresholdValue = {}'.format(threshold_value))
    print('output = {}'.format(output_folder))
    
    # Get list of input images
    images = listdir(input_images)
    
    # Threshold images
    for i in range(len(images)):
        image = images[i]
        print('*** Processing ' + image)
        # Open current image
        image_data = skimage.io.imread(join(input_images, image))
        # Threshold image
        binary = image_data > threshold_value
        # Save as 8bit tiled tiff
        skimage.io.imsave(join(output_folder, image), binary.astype(np.uint8), 'tifffile', False, tile=(1024,1024))
        print('Done')

if __name__ == "__main__":
    main()