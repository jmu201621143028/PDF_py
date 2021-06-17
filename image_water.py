import fitz

# https://pymupdf.readthedocs.io/en/latest/page.html#Page.insert_image

input_file = "test.pdf"
output_file = "output.pdf"
water_img = "water.png"

pix = fitz.Pixmap(water_img)
pix = fitz.Pixmap(pix, 1)
alpha = 255  #透明度
for i in range(pix.height):
	for j in range(pix.width):
		pixel = list(pix.pixel(j, i))
		if pixel == [255, 255, 255, 255]:
			pixel = [0, 0, 0, 0]
		else:
			pixel[-1] = alpha
		pix.setPixel(j, i, pixel)

doc = fitz.open(input_file)
num = len(doc)
page = doc[0]
rect = page.rect
core = (rect.width / 3, rect.height / 3)
dir = [(i, j) for j in range(-1, 2) for i in range(-1, 2)]
#dir = [dir[8]]  #可以根据编号控制填充九宫格的位置

for k in dir:
	location = [core[0] + k[0]*core[0], core[1] + k[1]*core[1]]
	location_ = [location[0] + core[0], location[1] + core[1]]
	image_rectangle = fitz.Rect(location, location_)
	page.insert_image(image_rectangle, pixmap=pix, rotate=90)

doc.save(output_file)
pass

