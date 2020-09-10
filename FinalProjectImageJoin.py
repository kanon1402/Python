from PIL import Image

img1 = Image.open("D:/Python/New training/Day2/day_2/Yst_rtn_RSMwise.png")
img2 = Image.open("D:/Python/New training/Day2/day_2/WhiteBackground.jpg")

width, height = img1.size
imageSize = Image.new('RGB', (1280, 480))
imageSize.paste(img1, (0, 0))
imageSize.paste(img2, (width, 0))

imageSize.save("RTN&White.png")
print("Two Image Join Success")
