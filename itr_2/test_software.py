import cv2
import numpy as np
import pandas as pd
import sys
from tkinter import Tk, filedialog

# Global variables
drawing = False  # True if the mouse is pressed
ix, iy = -1, -1
contours = []
circles = []
img_display = None
img = None  # Added global variable for the image
scale_factor = 1.0
draw_mode = 'freehand'  # Initial draw mode

def resize_image(image, max_height=800, max_width=1200):
    """
    Resize the image to fit within max_height and max_width while maintaining aspect ratio.
    """
    global scale_factor
    height, width = image.shape[:2]
    if height > max_height or width > max_width:
        scale = min(max_height / height, max_width / width)
        image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        scale_factor = scale
    return image

# Mouse callback function for freehand drawing
def draw_freehand(event, x, y, flags, param):
    global ix, iy, drawing, contours

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        contours.append([(int(x / scale_factor), int(y / scale_factor))])

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img_display, (ix, iy), (x, y), (0, 255, 0), 2)
            ix, iy = x, y
            contours[-1].append((int(x / scale_factor), int(y / scale_factor)))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img_display, (ix, iy), (x, y), (0, 255, 0), 2)
        contours[-1].append((int(x / scale_factor), int(y / scale_factor)))

# Mouse callback function for drawing circles
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, circles, img_display, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_display = resize_image(img.copy())  # Refresh the image
            radius = int(np.sqrt((x - ix)**2 + (y - iy)**2))
            num_dashes = 20  # Adjust the number of dashes
            dash_length = 5  # Adjust the length of each dash
            angle_step = 2 * np.pi / num_dashes
            for i in range(num_dashes):
                angle = i * angle_step
                x1 = int(ix + radius * np.cos(angle))
                y1 = int(iy + radius * np.sin(angle))
                x2 = int(ix + radius * np.cos(angle + angle_step))
                y2 = int(iy + radius * np.sin(angle + angle_step))
                cv2.line(img_display, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Dotted line

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        radius = int(np.sqrt((x - ix)**2 + (y - iy)**2))
        circles.append([(int(ix / scale_factor), int(iy / scale_factor), int(radius / scale_factor))])
        cv2.circle(img_display, (ix, iy), radius, (0, 0, 255), -1)  # Solid circle
        cv2.circle(img_display, (ix, iy), radius, (255, 255, 255), 2)  # Circle outline

def save_contours_and_circles_to_csv(contours, circles, file_name):
    flat_contours = [item for sublist in contours for item in sublist]
    df_contours = pd.DataFrame(flat_contours, columns=['x', 'y'])

    flat_circles = [item for sublist in circles for item in sublist]
    df_circles = pd.DataFrame(flat_circles, columns=['center_x', 'center_y', 'radius'])

    df = pd.concat([df_contours, df_circles], axis=1)
    df.to_csv(file_name, index=False)

def select_image(file_path):
    global img_display, contours, circles, img
    img = cv2.imread(file_path)
    if img is None:
        print("Error: Image not found.")
        return
    contours = []  # Clear existing contours when a new image is loaded
    circles = []   # Clear existing circles when a new image is loaded
    img_display = resize_image(img.copy())
    cv2.namedWindow('Image')

# Check if an image file path is provided as a command-line argument
if len(sys.argv) > 1:
    image_path = sys.argv[1]
    select_image(image_path)
else:
    print("Error: Please provide an image file path as a command-line argument.")
    sys.exit(1)

while True:
    if draw_mode == 'freehand':
        cv2.setMouseCallback('Image', draw_freehand)
    elif draw_mode == 'circle':
        cv2.setMouseCallback('Image', draw_circle)

    cv2.imshow('Image', img_display)
    key = cv2.waitKey(20) & 0xFF
    if key == 27:
        break
    elif key == ord('s'):
        save_contours_and_circles_to_csv(contours, circles, 'contours_and_circles.csv')
        print("Contours and circles saved to contours_and_circles.csv")
    elif key == ord('o'):
        if len(sys.argv) > 1:
            image_path = sys.argv[1]
            select_image(image_path)
        else:
            print("Error: Please provide an image file path as a command-line argument.")
    elif key == ord('f'):
        draw_mode = 'freehand'
        print("Switched to freehand drawing")
    elif key == ord('c'):
        draw_mode = 'circle'
        print("Switched to drawing circles")

cv2.destroyAllWindows()
