import streamlit as st
import streamlit.components.v1 as components

# Example usage of a custom HTML component
html_content = """
<div style="padding: 20px; background-color: #eef; border-radius: 8px;">
    <iframe src="https://calendar.google.com/calendar/embed?src=fed541c40f5d89f372ed5bf629b6e4041144e74b462bf3d3b12157f789e053cb%40group.calendar.google.com&ctz=Asia%2FHo_Chi_Minh" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
</div>
"""

# Render the HTML using components
components.html(html_content, height=150)

# Example of using HTML in Streamlit
st.title("Streamlit HTML Component Example")

# Custom HTML content
html_content = """
<iframe src="https://calendar.google.com/calendar/embed?src=fed541c40f5d89f372ed5bf629b6e4041144e74b462bf3d3b12157f789e053cb%40group.calendar.google.com&ctz=Asia%2FHo_Chi_Minh" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
"""

# Display the HTML content in Streamlit
components.html(html_content, height=200)