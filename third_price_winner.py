# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:02:21 2023

@author: aspirex99
"""

import base64
import streamlit as st
import plotly.express as px

df = px.data.iris()

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


#img = get_img_as_base64(r"https://gcdnb.pbrd.co/images/YtAsRPjbYOLF.gif?o=1")
x = " "

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://gcdnb.pbrd.co/images/zCP5k1UzwLGR.gif?o=1");
background-size: 99%;
background-position: top center;
background-repeat: non-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
#background-image: url("data:image/png;base64,{x}");
background-position: center center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

#-------------------------------------------------------Button---------------------------------------

# CSS and HTML to center-align the button and customize its appearance
centered_button = """
<style>
.center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Adjust this value to control vertical alignment */
}

.center button {
    width: 150px; /* Adjust the width to make the button larger */
    height: 150px; /* Adjust the height to make the button larger */
    border-radius: 50%; /* Make the button circular */
    background-color: #007BFF; /* Set the background color */
    color: white; /* Set the text color */
    font-size: 16px; /* Adjust the font size */
    cursor: pointer;
}
</style>

<div class="center">
    <button id="showImage">Show Image</button>
    <img id="giphyImage" style="display: none; max-width: 300px;" src="https://i.giphy.com/media/VRhsYYBw8AE36/200w.webp" alt="Giphy Image">
</div>

<script>
    document.getElementById("showImage").addEventListener("click", function() {
        // Show the Giphy image
        document.getElementById("giphyImage").style.display = "block";

        // After a delay of 5 seconds, hide the button
        setTimeout(function() {
            document.getElementById("showImage").style.display = "none";
        }, 5000);
    });
</script>
"""

st.markdown(centered_button, unsafe_allow_html=True)


#-----------------------------------------------------------------------------------------