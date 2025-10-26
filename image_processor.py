from PIL import Image
import numpy as np
import os

IMAGE_FILENAME = "sample_input.png"

def create_dummy_image(filename="sample_input.png"):
    """Creates a simple, small 10x10 grayscale image if a real one isn't found."""
    print(f"Image '{filename}' not found. Creating a dummy image to proceed.")
    # Create a 10x10 image with simple data (0-99)
    data = np.arange(100, dtype=np.uint8).reshape((10, 10))
    # 'L' mode is for grayscale (8-bit pixels)
    img = Image.fromarray(data, mode='L')
    img.save(filename)
    print("Dummy image saved successfully.")

def image_to_matrix(filename):
    """Loads an image and converts it into a NumPy matrix (array)."""
    
    if not os.path.exists(filename):
        create_dummy_image(filename)

    try:
        # 1. Load the image using Pillow
        img = Image.open(filename)
        print(f"Successfully loaded image '{filename}'. Format: {img.format}, Mode: {img.mode}, Size: {img.size}")

        # 2. Convert the image to a NumPy array (the matrix)
        image_matrix = np.array(img)

        # 3. Output the results
        print("\n--- Image Matrix Conversion Results ---")
        print(f"Matrix Shape (Height, Width, Channels): {image_matrix.shape}")
        print(f"Data Type (Dtype): {image_matrix.dtype}")
        
        # Print a small snippet of the matrix for visualization
        print("\nSnippet of the Image Matrix (top-left 5x5 pixels):")
        if len(image_matrix.shape) == 3: # Color image (H, W, C)
            print(image_matrix[:5, :5, 0]) # Show first channel (e.g., Red)
        else: # Grayscale image (H, W)
            print(image_matrix[:5, :5])

    except Exception as e:
        print(f"An error occurred during image processing: {e}")
        exit(1) # Fail the action on error

if __name__ == "__main__":
    image_to_matrix(IMAGE_FILENAME)