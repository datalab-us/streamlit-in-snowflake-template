import streamlit as st
import streamlit.components.v1 as components
from functions.style import apply_global_styles, apply_widget_styles, apply_advanced_styles

# 1. Configuration (Note: Limitations in SiS)
# st.set_page_config is supported but with limitations (e.g. page_title might be ignored in some contexts)
st.set_page_config(layout="wide", page_title="Snowflake Template")

# 2. Apply Centralized Styles
# Best Practice: Apply consistent styling across your app using reusable CSS blocks
apply_global_styles()
apply_widget_styles()
apply_advanced_styles()

# Header
st.title(":blue[Snowflake Streamlit Template]")
st.markdown("""
This template demonstrates **best practices** for styling Streamlit apps in Snowflake (SiS).
It implements a custom UI that matches the Snowflake native dark theme.
""")

st.markdown("---")

# 3. Built-in Color Text Support
st.header("1. Built-in Color Text Support")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(":blue[**This is blue text**] used for primary emphasis.")
with col2:
    st.markdown(":green[**This is green text**] used for success messages.")
with col3:
    st.markdown(":orange[**This is orange text**] used for warnings.")

st.markdown("---")

# 4. Styled Widgets
st.header("2. Styled Widgets")
st.markdown("These widgets are styled using custom CSS targeted at their specific classes.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Inputs")
    text_input = st.text_input("Styled Text Input", placeholder="Type something...")
    selectbox = st.selectbox("Styled Selectbox", ["Option 1", "Option 2", "Option 3"])

with col2:
    st.subheader("Buttons")
    st.button("Primary Button")
    st.button("Secondary Button")

st.markdown("---")

# 5. Advanced Styling Examples
st.header("3. Advanced Styling Examples")

# Info-Style Subheader using HTML/CSS class defined in style.py
st.markdown('<div class="info-style-subheader">ℹ️ This is an Info-Style Subheader created with custom HTML/CSS</div>', unsafe_allow_html=True)

# Text Area with highlighting concept
st.text_area("Styled Text Area", "This text area matches the dark theme styling.")

st.markdown("""
You can also use custom classes to highlight specific parts of text if you render them as HTML:
<span class="highlight-number">123.45</span>
""", unsafe_allow_html=True)

st.markdown("---")

# 6. Custom HTML Components
st.header("4. Custom HTML Components")
st.markdown("Using `st.components.v1.html` for isolated components.")

components.html("""
<div style="background-color: rgb(39, 50, 64); padding: 20px; border-radius: 10px; border: 1px solid rgb(60, 75, 94);">
    <h3 style="color: rgb(189, 196, 213); margin-top: 0;">Custom HTML Component</h3>
    <p style="color: rgb(189, 196, 213);">This is a custom HTML component with inline CSS styling. It is isolated in an iframe.</p>
    <button style="background-color: rgb(89, 153, 248); color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Click Me</button>
</div>
""", height=150)

st.markdown("---")

# 7. Metrics
st.header("5. Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Revenue", "$1.2M", "5%")
col2.metric("Users", "5.4K", "-2%")
col3.metric("Satisfaction", "98%", "1%")
