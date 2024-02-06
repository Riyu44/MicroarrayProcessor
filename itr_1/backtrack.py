import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('low_resolution_with_barcodes_no_duplicates_pink_circle_5.csv')

# Extract the pixel coordinates
x_values = data['x']
y_values = data['y']

# Read the image
image_path = 'fullres_modified.png'  # Replace with your image path
image = plt.imread(image_path)

# Display the image
plt.imshow(image)

# Highlight the pixel coordinates
plt.scatter(x_values, y_values, color='red', s=10)  # You can adjust the size (s) and color as needed

# Show the image with highlighted points
plt.show()

