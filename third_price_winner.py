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
centered_content = """
<style>
.center {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 120vh;
}

.center .giphy-container {
    margin-bottom: 20px;
}

.center .button-container {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
}

.center button {
    width: 80px;
    height: 40px;
    border-radius: 40%;
    background-color: #007BFF;
    color: white;
    font-size: 16px;
    cursor: pointer;
    margin: 10px;
}

.center img {
    max-width: 300px;
}
</style>

<div class="center">
    <div class="giphy-container">
        <img id="giphy-image" src="https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1" alt="Giphy Image">
    </div>
    <div class="button-container">
        <button id="back-button">Back</button>
        <button id="next-button">Next</button>
        <button id="redirect-button">Home</button>
    </div>
</div>

<script>
    const images = [
        "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1",
        "https://gcdnb.pbrd.co/images/g4rsoDUZqbEn.gif?o=1",
        "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1",
        "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1",
        "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1",
        "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1"
    ];

    const giphyImage = document.getElementById("giphy-image");
    const backButton = document.getElementById("back-button");
    const nextButton = document.getElementById("next-button");
    const redirectButton = document.getElementById("redirect-button");
    let currentIndex = 0;

    // Function to update the image
    function updateImage() {
        giphyImage.src = images[currentIndex];
    }

    // Event listeners for the buttons
    backButton.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateImage();
    });

    nextButton.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % images.length;
        updateImage();
    });

    // Redirect button behavior
    redirectButton.addEventListener("click", () => {
        window.open("https://coromandelhomepage-mflc32l5kyroxhjbxshxga.streamlit.app/", "_blank");
    });

    // Initial image update
    updateImage();
</script>
"""

st.markdown(centered_content, unsafe_allow_html=True)


#-----------------------------------------------------------------------------------------
