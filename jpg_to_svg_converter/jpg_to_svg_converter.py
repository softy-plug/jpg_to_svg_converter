import os
from PIL import Image

def convert_image(input_path, output_folder):
    with Image.open(input_path) as im:
        svg_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".svg")
        im.save(svg_path, format="SVG", quality=100)

def main():
    print("Welcome to JPG to SVG Converter!")
    jpg_folder = input("Enter the path to the folder containing JPG images: ")
    while not os.path.exists(jpg_folder):
        jpg_folder = input("The folder doesn't exist. Please enter a valid path to the JPG folder: ")
    svg_folder = input("Enter the path to the folder where converted SVG images will be saved: ")
    while not os.path.exists(svg_folder):
        svg_folder = input("The folder doesn't exist. Please enter a valid path to the SVG folder: ")
    # Create the SVG folder if it doesn't exist yet
    if not os.path.exists(svg_folder):
        os.makedirs(svg_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            convert_image(input_path, svg_folder)
    print("All images converted successfully to SVG format and saved in the chosen folder!")


if __name__ == "__main__":
    main()

# softy_plug