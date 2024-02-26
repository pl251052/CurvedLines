# Import necessary libraries
import cv2
import imutils  # helps manipulate a lot of OpenCV
import numpy as np


def detect_lines(image, filtered_image):
    # Find the contours (points with color/edges) in the image given which will be filtered and cropped
    contours, hierarchy = cv2.findContours(filtered_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours((contours, hierarchy))
    # Makes a list of the points
    lines = list(contours)
    lines.sort(key=cv2.contourArea)

    if len(lines) > 3:
        # Detects and draws all lines detected
        x1, x2, x3, x4 = lines[-4], lines[-3], lines[-2], lines[-1]
        cv2.drawContours(image, contours, -1, (0, 0, 0), 13) # really thick to cover the 2 lines
        # Saves and draws 4 lines detected
        line1 = cv2.approxPolyDP(x1, 4, False)
        cv2.drawContours(image, [line1], -1, (0, 0, 0), 6)

        line2 = cv2.approxPolyDP(x2, 4, False)
        cv2.drawContours(image, [line2], -1, (0, 0, 0), 6)

        line3 = cv2.approxPolyDP(x3, 4, False)
        cv2.drawContours(image, [line3], -1, (0, 0, 0), 6)

        line4 = cv2.approxPolyDP(x4, 4, False)
        cv2.drawContours(image, [line4], -1, (0, 0, 0), 6)

        midlines = []

        # Finds and draws midlines between 1st and 2nd as well as 3rd and 4th lines detected
        for line in [(line1[:int(len(line1) / 1.75)], line2),
                     (line3[:int(len(line3) / 1.75)], line4)]:
            midline = []
            for ln1, ln2 in zip(line[0], line[1]):
                mid_x = int((ln1[0][0] + ln2[0][0]) / 2)
                mid_y = int((ln1[0][1] + ln2[0][1]) / 2)
                midline.append([[mid_x, mid_y]])

            midline = np.array(midline, dtype=np.int32)
            cv2.polylines(image, [midline], False, (0, 0, 0), 5)
            midlines.append(midline)

        final_midline = []
        # Finds the midline of the above midlines
        for ln1, ln2 in zip(midlines[0], midlines[1]):
            mid_x = int((ln1[0][0] + ln2[0][0]) / 2)
            mid_y = int((ln1[0][1] + ln2[0][1]) / 2)
            final_midline.append([[mid_x, mid_y]])

        final_midline = np.array(final_midline, dtype=np.int32)
        cv2.polylines(image, [final_midline], False, (0, 0, 0), 5)

    # Draws a recactangle around the mask to show where it is
    cv2.rectangle(image, (500, 180), (1420, 900), (255, 255, 0), 3)
    return image