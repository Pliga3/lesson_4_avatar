from PIL import Image

image = Image.open("monro.jpg")
(red, green, blue) = image.split()

red1 = red.crop((50, 0, 696, 522))
red2 = red.crop((25,0,671, 522))
red3 = Image.blend(red1, red2, 0.5)

blue1 = blue.crop((0,0,646, 522))
blue2 = blue.crop((25,0,671, 522))
blue3 = Image.blend(blue1, blue2, 0.5)

green1 = green.crop((25,0,671, 522))

new_image = Image.merge("RGB", (red3, green1, blue3))
new_image.thumbnail((80, 80))

new_image.save("avatar.jpg")