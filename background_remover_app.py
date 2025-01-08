 import streamlit as st
from rembg import remove
from PIL import Image
import io

# Set up the Streamlit app
st.title("Background Remover")

# File uploader to allow image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)

    # Display the original image
    st.image(image, caption="Original Image", use_column_width=True)

    # Remove the background
    processed_image = remove(image)

    # Display the processed image
    st.image(processed_image, caption="Processed Image", use_column_width=True)

    # Prepare to download processed image
    buf = io.BytesIO()
    processed_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Download button
    st.download_button(
        label="Download Image",
        data=byte_im,
        file_name="processed_image.png",
        mime="image/png"
    )