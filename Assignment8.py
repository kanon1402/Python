import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

left, width = 0.0, .19
bottom, height = 0, 1
right = left + width
top = 1

fig = plt.figure(figsize=(6, 4))
ax = fig.add_axes([0, 0, 1, 1])  # Left, Bottom, Width, Height

for item in [fig, ax]:
    item.patch.set_visible(False)
    fig.patch.set_visible(False)
    ax.axis('off')

p = patches.Rectangle(
    (left, bottom), width, height,
    color='y'
)
ax.add_patch(p)


kpi_label = 'MHK'
retuen_p = '125K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)
ax.text(.5 * (left + right), .3 * (bottom + top), retuen_p,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

left, width = .20, .19
bottom, height = .0, 1
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#6a9aba'
)
ax.add_patch(p)

kpi_label2 = 'FRD'
retuen_p2 = '80K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label2,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)
ax.text(.5 * (left + right), .3 * (bottom + top), retuen_p2,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

left, width = .40, .19
bottom, height = .0, 1
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#39116e'
)
ax.add_patch(p)

kpi_label3 = 'RNG'
retuen_p3 = '240K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label3,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)
ax.text(.5 * (left + right), .3 * (bottom + top), retuen_p3,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

left, width = .60, .19
bottom, height = .0, 1
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#e15da7'
)
ax.add_patch(p)

kpi_label4 = 'MOT'
retuen_p4 = '180K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label4,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)
ax.text(.5 * (left + right), .3 * (bottom + top), retuen_p4,
        ha='center', va='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

left, width = .80, .20
bottom, height = .0, 1
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#98520d'
)
ax.add_patch(p)

kpi_label5 = 'MIR'
retuen_p5 = '45K'
ax.text(.5 * (left + right), .55 * (bottom + top), kpi_label5,
        ha='center', va='center',
        fontsize=24, color='Black',
        transform=ax.transAxes)
ax.text(.5 * (left + right), .3 * (bottom + top), retuen_p5,
        ha='center', va='center',
        fontsize=24, color='Black',
        transform=ax.transAxes)
plt.savefig('Assignment8.png')

img1 = Image.open("D:/Python/New training/Day2/day_2/Assignment8.png")
img2 = Image.open("D:/Python/New training/Day2/day_2/task.png")

width, height = img1.size
imageSize = Image.new('RGB', (1200, 800))
imageSize.paste(img1, (0, 0))
imageSize.paste(img2, (0, height))

imageSize.save("Assignment Join Image.png")
print("Two Image Join Success")
print('Complete')
img = Image.open("D:/Python/New training/Day2/day_2/Two Join Image.png")
img.show()



