
from PIL import Image, ImageFont, ImageDraw

titles = [
  "how to generate thumbnail",
  "how to make chatbot"
]

# create thumbnail 
def create_thumbnail():
	width = 1280
	height = 720
	return Image.new(mode = 'RGB', size = (width, height), color = 'rgb(52, 152, 219)')

# add text to thumbnail
def generate_thumbnail():
	thumbnail = create_thumbnail()
	for title in titles:
		text = title.split(' ')
		draw = ImageDraw.Draw(thumbnail)
		font = ImageFont.truetype('font/Roboto-Bold.ttf', 100)
		draw.text((50, 50), ' '.join(text[0 : 2]), fill = (50, 50, 50), font = font)
		draw.text((50, 150), ' '.join(text[0 :]), fill = (50, 50, 50), font = font)
		thumbnail.save(f"images/{title}.jpg")
		# create new thumbnail
		thumbnail = create_thumbnail()

generate_thumbnail()