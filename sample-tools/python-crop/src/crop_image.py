# NIST-developed software is provided by NIST as a public service. You may use, copy and distribute copies of the software in any medium, provided that you keep intact this entire notice. You may improve, modify and create derivative works of the software or any portion of the software, and you may copy and distribute such modifications or works. Modified works should carry a notice stating that you changed the software and should note the date and nature of any such change. Please explicitly acknowledge the National Institute of Standards and Technology as the source of the software.
# NIST-developed software is expressly provided "AS IS." NIST MAKES NO WARRANTY OF ANY KIND, EXPRESS, IMPLIED, IN FACT OR ARISING BY OPERATION OF LAW, INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT AND DATA ACCURACY. NIST NEITHER REPRESENTS NOR WARRANTS THAT THE OPERATION OF THE SOFTWARE WILL BE UNINTERRUPTED OR ERROR-FREE, OR THAT ANY DEFECTS WILL BE CORRECTED. NIST DOES NOT WARRANT OR MAKE ANY REPRESENTATIONS REGARDING THE USE OF THE SOFTWARE OR THE RESULTS THEREOF, INCLUDING BUT NOT LIMITED TO THE CORRECTNESS, ACCURACY, RELIABILITY, OR USEFULNESS OF THE SOFTWARE.
# You are solely responsible for determining the appropriateness of using and distributing the software and you assume all risks associated with its use, including but not limited to the risks and costs of program errors, compliance with applicable laws, damage to or loss of data, programs or equipment, and the unavailability or interruption of operation. This software is not intended to be used in any situation where a failure could cause risk of injury or damage to property. The software developed by NIST employees is not subject to copyright protection within the United States.
import numpy as np
#from PIL import Image
import skimage.io
import os
import argparse

"""
This class will crop each image in the input folder to fixed dimensions and save then in the output folder.

The arguments refer to the dimensions along x- and y-axes (xDim = width and yDim = height). 
The cropping is around the center of an image

__author__      = "Peter Bajcsy"
__email__ = "peter.bajcsy@nist.gov"
"""

def crop(crop_width, crop_height, basename, image_dir, output_dir):
    # in order to open images larger than limit of 178956970 pixels using Pillow library
    # based on https://stackoverflow.com/questions/56174099/how-to-load-images-larger-than-max-image-pixels-with-pil
    # Image.MAX_IMAGE_PIXELS = None

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    intensity_file = os.path.join(image_dir, basename)
    print('INFO: intensity_file:', intensity_file)
    if not os.path.isfile(intensity_file):
        print('ERROR: image does not exists:', intensity_file )
        return

    print('INFO: opening intensity image:', basename)
    # using Pillow library
    #intensity_im = Image.open(intensity_file)

    # using scikit-image library
    intensity_im = skimage.io.imread(intensity_file)

    # using Pillow library
    #imgwidth, imgheight = intensity_im.size

    # using scikit-image library
    imgwidth = intensity_im.shape[0]
    imgheight = intensity_im.shape[1]

    center_col = int(imgwidth/2)
    center_row = int(imgheight/2)
    if (center_col - int(crop_width/2)) < 0:
        leftupper_col = 0
    else:
        leftupper_col = center_col - int(crop_width/2)

    if (center_row - int(crop_height/2)) < 0:
        leftupper_row = 0
    else:
        leftupper_row = center_row - int(crop_height/2)

    if (leftupper_col + crop_width) > imgwidth or (leftupper_row + crop_height) > imgheight:
        print('ERROR: image dimensions are smaller than the requested crop dimensions for ', basename)
        return

    # using Pillow library
    #box = (leftupper_col, leftupper_row, leftupper_col + crop_width, leftupper_row + crop_height)
    #cropped = intensity_im.crop(box)

    # using scikit-image library
    cropped = intensity_im[leftupper_col:(leftupper_col + crop_width),leftupper_row:(leftupper_row + crop_height)]

    output_file = os.path.join(output_dir, basename)
    folder_name, file_extension = os.path.splitext(intensity_file)
    file_extension = file_extension[1:len(file_extension)]
    print('INFO: saving file extension ', file_extension)

    # using Pillow
    #a1.save(output_file, icc_profile=a1.info.get('icc_profile'))

    # Save as tiled tiff using skimage
    skimage.io.imsave(output_file, cropped.astype(intensity_im.dtype), 'tifffile', False, tile=(1024, 1024))



def crop_batch(image_dir, output_dir, xDim, yDim):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    i = 0
    for filename in os.listdir(image_dir):
        print('INFO: processing = ', filename)
        crop(xDim,yDim,filename, image_dir, output_dir)
        i += 1

def main():
    parser = argparse.ArgumentParser(prog='split', description='Script that crops images')
    parser.add_argument('--imagedir', type=str, required=True, help='folder path to input images')
    parser.add_argument('--outputdir', type=str, required=True, help='folder path to saving output tiles')
    parser.add_argument('--xDim', type=int, help='crop dimension in pixels along x-axis (width)')
    parser.add_argument('--yDim', type=int, help='crop dimension in pixels along y-axis (height)')
    args, unknown = parser.parse_known_args()

    if args.imagedir is None:
        print('ERROR: missing input image dir ')
        return

    if args.xDim is None:
        print('ERROR: missing x-dimension (width); default = 512 ')
        xDim = 512
    else:
        try:
            xDim = int(args.xDim)
        except ValueError:
            print('ERROR: x-dimension is not a number; default = 512 ')
            xDim = 512

    if args.yDim is None:
        print('ERROR: missing y-dimension (height); default = 512 ')
        yDim = 512
    else:
        try:
            yDim = int(args.yDim)
        except ValueError:
            print('ERROR: y-dimension is not a number; default = 512 ')
            yDim = 512

    if xDim < 0 or yDim < 0:
        print('ERROR: xDim or yDim is less than zero')
        return

    crop_batch(args.imagedir, args.outputdir, xDim, yDim)

if __name__ == "__main__":
    main()