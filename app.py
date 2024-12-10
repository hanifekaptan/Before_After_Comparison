import streamlit as st
import matplotlib.pyplot as plt
import leafmap.foliumap as leafmap
from io import BytesIO

st.title("BEFORE-AFTER COMPARISON")

st.write("Please upload the 'Before' and 'After' images.")

before = st.file_uploader("Upload the before image.", type=["jpg", "jpeg", "png"])

if before is not None:
    before_bytes = BytesIO(before.read())  # Read the image as bytes
    before_array = plt.imread(before_bytes, format=before.type)  # Load image into a numpy array

after = st.file_uploader("Upload the after image.", type=["jpg", "jpeg", "png"])

if after is not None:
    after_bytes = BytesIO(after.read())  # Read the image as bytes
    after_array = plt.imread(after_bytes, format=after.type)  # Load image into a numpy array

# Button to trigger the comparison
comparison = st.button("Comparison")

# If the comparison button is clicked
if comparison:
    # Generate the image comparison using leafmap
    leafmap.image_comparison(
        before_array,
        after_array,
        label1="before",
        label2="after",
        starting_position=50,
        out_html="image_comparison.html"
    )

    try:
        # Read the generated HTML file
        with open("image_comparison.html", 'r', encoding='ISO-8859-1') as HtmlFile:
            source_code = HtmlFile.read()
        
        # Display the HTML content in the Streamlit app
        st.components.v1.html(source_code, height=600)

        # Create a download button for the HTML file
        with open("image_comparison.html", "rb") as f:
            st.download_button(
                label="Download HTML File",
                data=f,
                file_name="image_comparison.html",
                mime="text/html"
            )
    except Exception as e:
        st.error(f"Error: {str(e)}")  # Show error message if something goes wrong