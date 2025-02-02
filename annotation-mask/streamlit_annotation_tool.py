# Script retirado do link:
#       https://towardsdatascience.com/build-a-data-annotation-pipeline-with-less-than-fifty-lines-of-code-with-streamlit-e72a3a84e259
#
# Esse script utiliza a biblioteca do streamlit para criar uma ferramenta 
# de anotaçãp manual de imagens. 

import streamlit as st
from PIL import Image
import os
import random


state = st.session_state

BASE_PATH = "./streamlit_images/"
OPTIONS = ["Anel de Sinete", "Normal"]

if "annotations" not in state:
    state.annotations = {}
    state.files = os.listdir(BASE_PATH)
    state.current_file = state.files[0]


def annotate(label):
    state.annotations[state.current_file] = label
    if state.files:
        state.current_file = random.choice(state.files)
        state.files.remove(state.current_file)


st.header("Dataset annotation")

if state.files:
    selected_file = state.current_file
    filename = os.path.join(BASE_PATH, selected_file)
    st.write(f"Current file: {selected_file}")
    image = Image.open(filename)
    st.image(image)

    c = st.columns(len(OPTIONS))
    for idx, option in enumerate(OPTIONS):
        c[idx].button(f"{option}", on_click=annotate, args=(option,))

else:
    st.info("Everything annotated.")

st.info(f"Annotated: {len(state.annotations)}, Remaining: {len(state.files)}")

st.download_button(
    "Download annotations as CSV",
    "\n".join([f"{k}\t{v}" for k, v in state.annotations.items()]),
    file_name="export.csv",
)