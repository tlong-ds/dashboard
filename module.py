import streamlit as st
import streamlit.components.v1 as components

def load_css():
    with open("./style/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def sidebar():
    sidebar_html = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <div class="custom-sidebar">
        <div class="logo"><img src="./app/static/logo.png" alt="Logo" class="logo"></div>
        <div class="menu-item"><a href="https://www.facebook.com/itsjkchan/"><i class="fab fa-facebook"></i></a></div>        
        <div class="menu-item"><a href="https://github.com/tlong-ds"><i class="fab fa-github"></i></a></div>
        <div class="menu-item"><a href="https://www.linkedin.com/in/thành-long-lý-565b6a341/"><i class="fab fa-linkedin"></i></a></div>
        <div class="menu-item"><a href="https://www.gmail.com"><i class="fas fa-envelope"></i></a></div>
        <div class="menu-item"><a href="#"><i class="fas fa-cogs"></i></a></div>
    </div>
    """
    st.markdown(sidebar_html, unsafe_allow_html=True)
    

def title(text: str):
    st.markdown(f'<div style="margin-left: 260px;"><h1>{text}</h1></div>', unsafe_allow_html=True)

def header(text: str):
    st.markdown(f'<div style="margin-left: 260px;"><h2>{text}</h2></div>', unsafe_allow_html=True)

def subheader(text: str):
    st.markdown(f'<div style="margin-left: 260px;"><h3>{text}</h3></div>', unsafe_allow_html=True)

def write(text: str):
    st.markdown(f'<div style="margin-left: 260px;">{text}</div>', unsafe_allow_html=True)

def space():
    st.markdown("")
    st.markdown("")
    st.markdown("")
    
@st.cache_data
def neu_calendar():
    html_content = """
    <div style="margin-left: 260px;">
    <iframe src="https://calendar.google.com/calendar/embed?src=fed541c40f5d89f372ed5bf629b6e4041144e74b462bf3d3b12157f789e053cb%40group.calendar.google.com&ctz=Asia%2FHo_Chi_Minh&mode=week" style="border: 0" width="500" height="500" frameborder="0" scrolling="yes"></iframe>
    </div>
    """
    header("Timetable")
    components.html(html_content, height = 500, width = 1000)