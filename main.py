import csv
from PIL import Image, ImageDraw, ImageFont

# Configuration
input_image = "Thiệp nhà Thúy (main).png"  # Path to your image
# input_image = "hanoi_invitation.png"  # Path to your image
csv_file = "names.csv"           # Path to the CSV file with names
font_path = "Dancing_Script/DancingScript-VariableFont_wght.ttf"          # Path to the .ttf font file
output_folder = csv_file.split(".")[0] # Folder to save the output images
font_size = 50                   # Desired font size
center_position = (1550, 458)         # (x, y) position for the text
text_color = (0, 0, 0)           # Text black 

# Load the font
font = ImageFont.truetype(font_path, font_size)

# Create output folder if it doesn't exist
import os
os.makedirs(output_folder, exist_ok=True)

# Read the names from the CSV
with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    names = [row[0] for row in reader]  # Assuming names are in the first column

# Process each name
for idx, name in enumerate(names):
    # Open the image
    with Image.open(input_image) as img:
        draw = ImageDraw.Draw(img)
        
        # Calculate text size
        text_bbox = font.getbbox(name)  # (left, top, right, bottom)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Adjust position to center the text
        text_x = center_position[0] - text_width // 2
        text_y = center_position[1] - text_height // 2
        centered_position = (text_x, text_y)

        # Add text to the image
        draw.text(centered_position, name, fill=text_color, font=font)
        
        # Save the output image
        output_path = os.path.join(output_folder, f"{name}.png")
        
        img.save(output_path)

print(f"Images saved in '{output_folder}' folder.")
