import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale converter")

#create a file uploader component allowing the user to upload a file
uploaded_image= st.file_uploader("Upload_image")

#this line gives more control over camera.
with st.expander("Start camera"):
    #start the camera
    camera_image = st.camera_input("Camera")
    print(camera_image)

if camera_image:
    #create a pollow image instance
    img = Image.open(camera_image)

    #convert the pillow image to grayscale
    gray_img = img.convert("L")

    #render the grayscale imgae on the webpage
    st.image(gray_img)

#check if the umage exists meaning the user has uploaded a file.
if uploaded_image:
    #open the user uploaded_image with PIL
    img=Image.open(uploaded_image)
    #convert the image to grayscale
    gray_uploaded_img= img.convert('l')
    #display the grayscale image on the webpage
    st.image(gray_uploaded_img)