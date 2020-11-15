# What is this used for?
# You shouldn't need to save an output image since you only need to count the number of powercells
# And send that number over network tables
from PIL import Image, ImageDraw
import numpy as np
from math import sqrt
import cv2
def Prototype():
# Load image:
    input_image = Image.open("input.png")
    input_pixels = input_image.load()
    width, height = input_image.width, input_image.height

    # Create output image
    output_image = Image.new("RGB", input_image.size)
    draw = ImageDraw.Draw(output_image)

    # Convert to grayscale
    intensity = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            intensity[x, y] = sum(input_pixels[x, y]) / 3

    # Compute convolution between intensity and kernels
    for x in range(1, input_image.width - 1):
        for y in range(1, input_image.height - 1):
            magx = intensity[x + 1, y] - intensity[x - 1, y]
            magy = intensity[x, y + 1] - intensity[x, y - 1]

            # Draw in black and white the magnitude
            color = int(sqrt(magx**2 + magy**2))
            draw.point((x, y), (color, color, color))
    
    output_image.save("edge.png")