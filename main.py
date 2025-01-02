import streamlit as st
from streamlit.components.v1 import html
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from module import *
st.set_page_config(
    page_title = "Dashboard",
    layout = "wide"
)

# Visual Handler
load_css()
sidebar()


def main():
    heading = "Ly Thanh Long"
    title("Welcome to 2025 Dashboard!")

    col1, col2 = st.columns([1, 2])
    
    with col1:
        header("Ly Thanh Long")
        write("Data Science in Economics and Business")
        write("2023-2027")
        space()
        neu_calendar()
    with col2:
        header("Meomeo")




if __name__ == "__main__":
    main()