import fitz
doc = fitz.open('test.pdf')  # new or existing PDF
page = doc[0]  # new or existing page via doc[n]
p = fitz.Point(50, 72)  # start point of 1st line

text = "fsdfafd张"
# the same result is achievable by
# text = ["Some text", "spread across", "several lines."]

rc = page.insert_text(p,  # bottom-left of 1st char
                     text,  # the text (honors '\n')
                     fontname = "china-s",  # the default font
                     fontsize = 20,  # the default font size
                     rotate = 0,  # also available: 90, 180, 270
                     stroke_opacity = 0.1,
                     fill_opacity = 1,
                     )
print("%i lines printed on page %i." % (rc, page.number))

doc.save("text.pdf")