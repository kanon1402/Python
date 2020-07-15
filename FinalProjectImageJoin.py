from PIL import Image

img1 = Image.open("D:/Python/New training/Day2/day_2/T3(Anwarhossain).png")
img2 = Image.open("D:/Python/New training/Day2/day_2/T3(Kamrulahsan).png")

width, height = img1.size
imageSize = Image.new('RGB', (1260, 480))
imageSize.paste(img1, (0, 0))
imageSize.paste(img2, (width, 0))

imageSize.save("T3(AnwarhossainKamrulahsan).png")
print("Two Image Join Success")
