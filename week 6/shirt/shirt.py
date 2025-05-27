import sys
import os
from PIL import Image, ImageOps  # Correct import for the Image module

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    check(input_file, output_file)
    process(input_file, output_file)

def check(input_file, output_file):
    if not input_file.endswith((".png", ".jpg", ".jpeg")):
        print("Invalid file type. Only PNG, JPG, and JPEG files are allowed.")
        sys.exit(1)

    # Check if the input file exists
    if not os.path.exists(input_file):
        print("File does not exist.")
        sys.exit(1)

    # Check if the extensions of input and output files match
    input_ext = os.path.splitext(input_file)[1]  # Get extension of input file
    output_ext = os.path.splitext(output_file)[1]  # Get extension of output file
    if input_ext != output_ext:
        print("Input and output file extensions do not match.")
        sys.exit(1)

def process(input_file, output_file):
    try:
        shirt = Image.open("shirt.png")  # Open the shirt.png image
        image = Image.open(input_file)

        # Resize the image to match the size of the shirt
        size = shirt.size # it is a tuple (600, 600)
        image = ImageOps.fit(image, size) # resize and crop the input


        # Create a copy of the image and paste the shirt on top (with transparency)
        image.paste(shirt, (0, 0), shirt)  # Third argument ensures transparency if available

        # Save the final image
        image.save(output_file)
        print(f"Processed image saved to {output_file}")
        sys.exit(0)
    except Exception as e:
        print(f"Error during processing: {e}")

if __name__ == "__main__":
    main()
