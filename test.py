from PIL import Image, ImageDraw

# Map dimensions (width, height)
map_size = (100, 100)

# Create a white image (free space)
map_image = Image.new("L", map_size, color=255)

# Draw obstacles
draw = ImageDraw.Draw(map_image)
draw.rectangle([20, 20, 40, 40], fill=0)  # Black square obstacle
draw.line([60, 20, 60, 40], fill=0, width=2)  # Black line obstacle

# Save the map image as a PNG file
map_image.save("map.png")
