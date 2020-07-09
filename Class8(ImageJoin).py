from PIL import Image

img1 = Image.open("D:/Python/New training/Day2/day_2/Donut_Chart.png")
img2 = Image.open("D:/Python/New training/Day2/day_2/linechart.png")
img3 = Image.open("D:/Python/New training/Day2/day_2/Assignment5.png")
img4 = Image.open("D:/Python/New training/Day2/day_2/task.png")

# img1.show()
# img2.show()
# img3.show()
# img4.show()

# # Join two image

# width, height = img1.size
# imageSize = Image.new('RGB', (1300, 480))
# imageSize.paste(img1, (0, 0))
# imageSize.paste(img2, (width, 0))
#
# imageSize.save("Two Join Image.png")
# print("Two Image Join Success")
# img = Image.open("D:/Python/New training/Day2/day_2/Two Join Image.png")
# img.show()

# # Join 4 image

# width, height = img1.size
# imageSize = Image.new('RGB', (1280, 960))
# imageSize.paste(img1, (0, 0))
# imageSize.paste(img2, (width, 0))
# imageSize.paste(img3, (0, height))
# imageSize.paste(img4, (width, height))
#
# imageSize.save("4 Join Image.png")
# print("4 Image Join Success")
# img = Image.open("D:/Python/New training/Day2/day_2/4 Join Image.png")
# img.show()
