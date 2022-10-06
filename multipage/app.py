import streamlit as st
import PIL


icon_load = PIL.Image.open("resources/page_icon.ico")

st.set_page_config(page_title="Multipage Test",page_icon=icon_load)

st.sidebar.success("Select a page")