import pandas as pd
from scipy.spatial import KDTree

# Load the CSV files
contours_df = pd.read_csv('contours.csv')
tissue_positions_df = pd.read_csv('tissue_positions.csv')

# Filter out entries where 'in_tissue' is not 1
tissue_positions_df = tissue_positions_df[tissue_positions_df['in_tissue'] == 1]

# Create a KDTree for efficient nearest neighbor search
tree = KDTree(tissue_positions_df[['pxl_col_in_fullres', 'pxl_row_in_fullres']])

# Find the nearest neighbor for each point in contours_df
closest_points_indices = tree.query(contours_df[['x', 'y']])[1]

# Extract the corresponding barcodes
closest_barcodes = tissue_positions_df.iloc[closest_points_indices]['barcode']

# Remove duplicate barcodes
unique_barcodes = closest_barcodes.drop_duplicates()

# Save the unique barcodes to a new CSV file
unique_barcodes.to_csv('barcodes.csv', index=False)

print("Unique barcodes have been saved to barcodes.csv")

