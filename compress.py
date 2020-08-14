from PIL import Image
import numpy as np

compression_factors = [8, 16, 32]
number = 411

for factor in compression_factors:
	for no in range(1, number + 1):
		pixels = []
		#input_name = "High.jpg"
		#output_name = "Output.jpg"
		name = str(no) + ".png"
		input_name = "Images/" + name
		output_name = "Compress_" + str(factor) + "/" + name
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
		print(str(factor) + ": " + str(no))