# Usage:
#
# python3 script.py --input original.png --output modified.png
# Based on: https://github.com/mostafaGwely/Structural-Similarity-Index-SSIM-

# 1. Import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
# from skimage.measure import structural_similarity as ssim
import numpy as np

# Calculate MSE


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    print(imageA)
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

# 2. Construct the argument parse and parse the arguments


ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="Directory of the image that will be compared")
ap.add_argument("-s", "--second", required=True, help="Directory of the image that will be used to compare")
args = vars(ap.parse_args())

# 3. Load the two input images
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])

# 4. Convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# 5. Compute the Mean Squared Error between the two
#    images, ensuring that the difference image is returned
mse_err = mse(grayA, grayB)

# diff = (diff * 255).astype("uint8")

# 6. You can print only the score if you want
print("MSE: {}".format(mse_err))
