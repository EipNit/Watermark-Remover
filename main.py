import os
from pathlib import Path
from PIL import Image
import numpy as np


# Set the input and output directories
input_dir = Path('image')
output_dir = Path('out')
output_dir.mkdir(exist_ok=True)  # Create output directory if it doesn't exist

# Function to remove watermark from an image
def remove_watermark(image_path, output_path):
    # Read the image
    img = Image.open(image_path).convert('RGB')
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Convert to grayscale
    gray_img = np.dot(img_array[..., :3], [0.2989, 0.5870, 0.1140])
    
    # Apply threshold
    threshold = 200
    max_value = 255
    watermark_removed_array = np.where(gray_img > threshold, max_value, gray_img)
    
    # Convert back to an image and save
    Image.fromarray(np.uint8(watermark_removed_array)).save(output_path)

# Iterate over all images in the input directory and process them
for image_file in input_dir.glob('*.png'):
    # Set the output path
    output_path = output_dir / f'{image_file.stem}_no_watermark.png'
    # Remove watermark
    remove_watermark(image_file, output_path)

# List the files in the output directory to verify
output_files = list(output_dir.glob('*_no_watermark.png'))
output_files
