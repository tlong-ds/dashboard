import streamlit as st
from streamlit.components.v1 import html
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
import subprocess
import matplotlib.pyplot as plt
from datetime import date
from sheets import create_task, update_task, read_google_sheet
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
        header("Task Management")
        df = read_google_sheet()
        if st.button("Create task"):
            create_task()
        
        c1, c2 = st.columns(2)
        with c1:
            subheader("Not Finished")
            if df is not None and 'Task' in df.columns:
                for i, task in enumerate(df['Task']):
                    if task:
                        a = st.checkbox(task, key=f"task_{i}", value = df[df['Task'] == task].iloc[0]['Checkbox']) 
                        clicked = False
                        if a and df[df['Task'] == task].iloc[0]['Checkbox'] == 0:
                            update_task(task, 1)
                            clicked = True
                        elif not a and df[df['Task'] == task].iloc[0]['Checkbox'] == 1 and clicked:
                            update_task(task, 0)
                            clicked = False
            else:
                st.write("No tasks available.")
        with c2:
            st.markdown(f'<div style="margin-left: 0px;"><h3>Progress</h3></div>', unsafe_allow_html=True)
            st.bar_chart(data = df, x = "Due", y = "Checkbox")

                    
        
            



if __name__ == "__main__":
    main()