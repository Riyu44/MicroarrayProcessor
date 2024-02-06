import pandas as pd
import numpy as np
from scipy.spatial import KDTree

# Load the CSV files
contours_df = pd.read_csv('contours_and_circles.csv')
tissue_positions_df = pd.read_csv('tissue_positions.csv')

# Filter out entries where 'in_tissue' is not 1
tissue_positions_df = tissue_positions_df[tissue_positions_df['in_tissue'] == 1]

# Function to check if a point is inside a circle
def is_inside_circle(point, center, radius):
    return np.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2) <= radius

# Initialize an empty list to store barcodes
barcodes = []

# Handle points with specific 'x' and 'y' coordinates
specific_points_df = contours_df.dropna(subset=['x', 'y'])
if not specific_points_df.empty:
    tree = KDTree(tissue_positions_df[['pxl_col_in_fullres', 'pxl_row_in_fullres']])
    closest_points_indices = tree.query(specific_points_df[['x', 'y']])[1]
    barcodes.extend(tissue_positions_df.iloc[closest_points_indices]['barcode'].tolist())

# Handle points defined by a circle
circle_points_df = contours_df.dropna(subset=['center_x', 'center_y', 'radius'])
for _, row in circle_points_df.iterrows():
    center = (row['center_x'], row['center_y'])
    radius = row['radius']
    for _, tissue_row in tissue_positions_df.iterrows():
        point = (tissue_row['pxl_col_in_fullres'], tissue_row['pxl_row_in_fullres'])
        if is_inside_circle(point, center, radius):
            barcodes.append(tissue_row['barcode'])

# Convert to DataFrame and remove duplicates
unique_barcodes = pd.DataFrame(set(barcodes), columns=['barcode'])

# Save the unique barcodes to a new CSV file
unique_barcodes.to_csv('barcodes_complete.csv', index=False)

print("Unique barcodes have been saved to barcodes_complete.csv")
