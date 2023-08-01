from PIL import Image, ImageDraw

image = Image.open("C:/Users/ppyol1/Documents/classes in python/phase_separation_example.png")
draw = ImageDraw.Draw(image)
draw.regular_polygon((360,320,302), 6,rotation=0, outline="red")
draw.regular_polygon((360,320,301), 6,rotation=0, outline="red")
draw.regular_polygon((360,320,300), 6,rotation=0, outline="red")
draw.regular_polygon((360,320,299), 6,rotation=0, outline="red")
draw.regular_polygon((360,320,298), 6,rotation=0, outline="red")
image.show()
image.save("annotated_hexagon.png")
