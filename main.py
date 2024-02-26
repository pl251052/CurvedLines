# Sources:
# Hough Line Transform Tutorial - https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
# Masking - https://stackoverflow.com/questions/11492214/opencv-via-python-is-there-a-fast-way-to-zero-pixels-outside-a-set-of-rectangle
# Sorting Contours - https://pyimagesearch.com/2015/04/20/sorting-contours-using-python-and-opencv/
# Contour Approximation - https://pyimagesearch.com/2021/10/06/opencv-contour-approximation/
# Hough Line Transform Tutorial - used for lines 7-10 of filter.py
# Masking - used for lines 14-19 in filter.py
# Sorting Contours - used in lines 9-13
# Contour Approximation - used in lines 17 - 30 of olines.py

# Import necessary files and functions
from filter import * # does masking and filtering
from olines import * # does line detecting and overlay, including middle line


# Saves video feed
videoCapture = cv2.VideoCapture(0)

while True:
    # Goes through each frame to process and overlay
    ret, frame = videoCapture.read()
    filtered = filter_image(frame) # filters image, further explanation in function definition
    masked = create_mask(filtered) # makes a mask around the wanted area
    cv2.imshow('Detected', detect_lines(frame, masked))
    if cv2.waitKey(1) == ord('q'):
        break
# When everything is done, release the capture
videoCapture.release()
cv2.destroyAllWindows()