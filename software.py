import cv2
import numpy as np
import pandas as pd

# Global variables
drawing = False # True if the mouse is pressed
ix, iy = -1, -1
contours = []

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

# Mouse callback function
def draw_contour(event, x, y, flags, param):
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

def save_contours_to_csv(contours, file_name):
    flat_list = [item for sublist in contours for item in sublist]
    df = pd.DataFrame(flat_list, columns=['x', 'y'])
    df.to_csv(file_name, index=False)


# Load the image
img = cv2.imread('fullres.jpg')
if img is None:
    print("Error: Image not found.")
    exit()


img_display = resize_image(img.copy())

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_contour)

while True:
    cv2.imshow('Image', img_display)
    key = cv2.waitKey(20) & 0xFF
    if key == 27:
        break
    elif key == ord('s'):
        save_contours_to_csv(contours, 'contours.csv')
        print("Contours saved to contours.csv")

cv2.destroyAllWindows()
