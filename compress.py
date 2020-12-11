#!/usr/bin/python3
from PIL import Image
import numpy as np
import sys

def compress(input_name, output_name, factor):
	pixels = []
	picture = Image.open(input_name)
	width, height = picture.size
	for x in range(width):
		row = []
		for y in range(height):
			new_pixel = []
			pixel = picture.getpixel((x,y))
			pixel = list(pixel)
			for i in pixel:
				if i % factor != 0:
					i = i - i % factor
				new_pixel.append(i)
			new_pixel = tuple(new_pixel)
			row.append(new_pixel)
		pixels.append(row)

	array = np.array(pixels, dtype=np.uint8)
	array = np.flip(array, 0)
	new_picture = Image.fromarray(array).rotate(270, expand = 1)
	new_picture.save(output_name)

if __name__ == "__main__":
	args = sys.argv
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	factor = 16
	if len(args) == 4:
		factor = int(sys.argv[3])
	compress(input_file, output_file, factor)
