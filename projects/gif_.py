import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "aa.gif",
    save_all=True,
    append_images=images[1:],
    duration=200,
    loop=0
)

# RUN: python gif_.py aa1.gif aa2.gif
# Then open aa.gif to view the result  