import fitz


def MakeImg4Doc(file):
	doc = fitz.open(file)
	for page in doc:
		pix = page.get_pixmap(alpha=False)
		pix.writePNG("page-{}.png".format(page.number))


def IncImgRes(file):
	# 简单的缩放
	zomm_x, zomm_y = 2.0, 2.0
	mat = fitz.Matrix(zomm_x, zomm_y)
	doc = fitz.open(file)
	page = doc[0]
	pix = page.get_pixmap(matrix=mat)
	pix.writePNG("page-zoom-{}.png".format(page.number))

def ClipsPdf(file):
	#给出左上角的位置和右下角的位置
	doc = fitz.open(file)
	page = doc[0]
	mat = fitz.Matrix(2, 2)
	rect = page.rect
	mp = (rect.tl + rect.br) / 2  #计算出中心点的位置
	clip = fitz.Rect(mp, rect.br)
	pix = page.get_pixmap(matrix=mat, clip=clip)
	pix.writePNG("page-clips-{}.png".format(page.number))
	doc.close()
	pass

def ExtractImg(file):
	doc = fitz.open(file)
	page = doc[2]
	d = page.get_text("dict")
	blocks = d["blocks"]
	imgblocks = [b for b in blocks if b["type"] == 1]
	pass


def GenImg():
	src = fitz.Pixmap('img-7edges.png')
	col = 3
	lin = 4
	tar_w = src.width * col
	tar_h = src.height * lin
	tar_pix = fitz.Pixmap(src.colorspace, (0, 0, tar_w, tar_h), src.alpha)
	for i in range(col):
		for j in range(lin):
			src.setOrigin(src.width * i, src.height * j)
			tar_pix.copyPixmap(src, src.irect)
	tar_pix.writePNG("tar.png")
	pass

def insert_img():
	doc = fitz.open(r'01-CS107-Course-Information_4221_8729.pdf')
	rect = fitz.Rect(0, 0, 50, 50)
	img = open("some.jpg", "rb").read()  # an image file

if __name__ == "__main__":
	file = r'01-CS107-Course-Information_4221_8729.pdf'
	# IncImgRes(file)
	# ClipsPdf(file)
	# ExtractImg(file)
	GenImg()