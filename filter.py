# Import necessary libraries
import cv2
import numpy as np

def filter_image(image):
    # Coverts the image to grayscale, blurs it, and then uses canny edge to detect the edges
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray_image, (3, 3), 0)
    edges = cv2.Canny(blur, threshold1=150, threshold2=82.5, apertureSize=3)
    return edges

def create_mask(img):
    # Creates a mask using the vertices below (remember the y coordinates work opposite the coordinate grid)
    left, top, right, bot = 500, 180, 1420, 900
    mask_vertices = [(left, top), (right, top), (right, bot), (left, bot)]
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, np.array([mask_vertices], np.int32), 255)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image