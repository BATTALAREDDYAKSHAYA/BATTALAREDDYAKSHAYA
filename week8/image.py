from PIL import Image

# Open an image file
image_path = ''
image = Image.open('/home/rguktrkvalley/Pictures/Wallpapers/WhatsApp Image 2024-01-20 at 9.29.18 PM.jpeg')

# Get RGB values of the pixel at position (x, y)
x, y = 100, 100
rgb = image.getpixel((x, y))
print(f'RGB values at position ({x}, {y}): {rgb}')

# Set RGB values of the pixel at position (x, y) to new values
new_rgb = (255, 0, 0)  # Example: set to red
image.putpixel((x, y), new_rgb)

# Save the modified image to a new file
output_path = '/home/rguktrkvalley/Pictures/Wallpapers/WhatsApp Image 2024-01-20 at 9.29.18 PM.jpeg'
image.save(output_path)

# Close the image
image.close()
