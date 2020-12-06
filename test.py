import numpy as np
import cv2

from main import count_powercells

# Run the count_powercells function and get the return value
# Return value example (delete line below)
# Print out that return value
img = cv2.imread("Sheraz.png")
powercell_count = count_powercells(img, img)
print("Powercell count: " + str(powercell_count))

