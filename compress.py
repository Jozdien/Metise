from PIL import Image
import numpy as np

pixels = []
compression_factor = 64

picture = Image.open("High.jpg")
width, height = picture.size
for x in range(width):
	row = []
	for y in range(height):
		new_pixel = []
		pixel = picture.getpixel((x,y))
		pixel = list(pixel)
		for i in pixel:
			if i % compression_factor != 0:
				i = i - i % compression_factor
			new_pixel.append(i)
		new_pixel = tuple(new_pixel)
		row.append(new_pixel)
	pixels.append(row)

array = np.array(pixels, dtype=np.uint8)
array = np.flip(array, 0)
new_picture = Image.fromarray(array).rotate(270, expand = 1)
new_picture.save('New.jpg')