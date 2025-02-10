import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# Function to overlay text on an image
def add_text_to_image(image, text):
    # Load a font
    font_size = 70                   # Desired font size
    center_position = (1550, 450)         # (x, y) position for the text
    text_color = (229, 51, 97)   
    try:
        font = ImageFont.truetype("Dancing_Script/DancingScript-VariableFont_wght.ttf", font_size)  # You can replace with any font file
    except IOError:
        font = ImageFont.load_default()

    # Create an ImageDraw object to add text
    draw = ImageDraw.Draw(image)

    # Calculate text size
    text_bbox = font.getbbox(text)  # (left, top, right, bottom)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    # Adjust position to center the text
    text_x = center_position[0] - text_width // 2
    text_y = center_position[1] - text_height // 2
    centered_position = (text_x, text_y)

    # Add text to the image
    draw.text(centered_position, text, fill=text_color, font=font)
    
    return image

# Streamlit app
def main():
    input_image = "hanoi_invitation.png"  # Path to your image
    st.title("App tạo thiệp cưới")
    
    
        # Open the image with Pillow
    with Image.open(input_image) as image:
        # Get text input from the user
        text = st.text_input("Điền chữ vào thiệp:", value="", key="text_input")
        
        if text:
            # Add the text to the image
            image_with_text = add_text_to_image(image.copy(), text)
            
            # Display the image with text
            st.image(image_with_text, caption="Ảnh sau khi ghép chữ: ", use_container_width=True)
            
            # Allow user to download the image with text
            buffer = io.BytesIO()
            image_with_text.save(buffer, format="PNG")
            buffer.seek(0)
            
            st.download_button(
                label="Tải ảnh về",
                data=buffer,
                file_name=f"{text}.png",
                mime="image/png"
            )

# Run the app
if __name__ == "__main__":
    main()
