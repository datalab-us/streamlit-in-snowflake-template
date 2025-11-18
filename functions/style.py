import streamlit as st

def apply_global_styles():
    """
    Applies global styles to match Snowflake's native theme (Light & Dark support).
    Best Practice: Use CSS variables and @media (prefers-color-scheme).
    """
    st.markdown("""
    <style>
    /* Import Lato font from Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&display=swap');
    
    :root {
        /* Default to Dark Mode (Snowflake Native Dark) */
        --sf-bg-color: rgb(28, 37, 48);
        --sf-text-color: rgb(189, 196, 213);
        --sf-sidebar-bg-color: rgb(28, 37, 48);
        --sf-border-color: rgb(60, 75, 94);
        --sf-input-bg-color: rgb(39, 50, 64);
        --sf-primary-color: #29B5E8; /* Snowflake Blue */
        --sf-primary-hover-color: #11567F; /* Mid Blue */
        --sf-accent-orange: #FF9F36; /* Valencia Orange */
    }

    @media (prefers-color-scheme: light) {
        :root {
            /* Light Mode (Snowflake Native Light) */
            --sf-bg-color: #FFFFFF;
            --sf-text-color: #24323D; /* Winter */
            --sf-sidebar-bg-color: #F5F6F7;
            --sf-border-color: #E0E0E0;
            --sf-input-bg-color: #FFFFFF;
            /* Primary colors remain the same */
        }
    }
    
    /* Global Styles */
    .stApp {
        background-color: var(--sf-bg-color);
        color: var(--sf-text-color);
        font-family: 'Lato', sans-serif;
    }
    
    /* Text coloring */
    h1, h2, h3, h4, h5, h6, p, li, div, span {
        color: var(--sf-text-color);
        font-family: 'Lato', sans-serif;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: var(--sf-sidebar-bg-color);
        border-right: 1px solid var(--sf-border-color);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: var(--sf-text-color);
    }
    
    /* Links */
    a {
        color: var(--sf-primary-color);
        text-decoration: none;
    }
    a:hover {
        color: var(--sf-primary-hover-color);
    }
    </style>
    """, unsafe_allow_html=True)

def apply_widget_styles():
    """
    Applies custom styles to specific widgets using CSS variables.
    """
    st.markdown("""
    <style>
    /* Custom CSS for text input widget */
    .stTextInput > div > div > input {
        background-color: var(--sf-input-bg-color);
        color: var(--sf-text-color);
        border: 1px solid var(--sf-border-color);
        border-radius: 4px;
        font-family: 'Lato', sans-serif;
    }
    .stTextInput > div > div > input:focus {
        border-color: var(--sf-primary-color);
        outline: none;
    }

    /* Style the selectbox */
    .stSelectbox > div > div > div {
        background-color: var(--sf-input-bg-color);
        color: var(--sf-text-color);
        border: 1px solid var(--sf-border-color);
        border-radius: 4px;
        font-family: 'Lato', sans-serif;
    }
    
    /* Button Styling - Pill Shape, All Caps, Snowflake Blue */
    .stButton > button {
        background-color: var(--sf-primary-color);
        color: white;
        border: none;
        border-radius: 80px; /* Pill shape per brand guide */
        padding: 12px 27px; /* Per brand guide specs */
        font-family: 'Lato', sans-serif;
        font-weight: 900; /* Heavy/Bold */
        text-transform: uppercase;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: var(--sf-primary-hover-color);
        border-color: var(--sf-primary-hover-color);
    }
    
    /* Metric Styling */
    [data-testid="stMetricValue"] {
        color: var(--sf-text-color);
        font-family: 'Lato', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

def apply_advanced_styles():
    """
    Demonstrates advanced styling like Info-Style Subheaders.
    """
    st.markdown("""
    <style>
    .info-style-subheader {
        background-color: rgba(41, 181, 232, 0.1); /* Snowflake Blue with opacity */
        color: var(--sf-primary-color);
        padding: 16px 20px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        border: 1px solid rgba(41, 181, 232, 0.2);
        margin-bottom: 20px;
        font-family: 'Lato', sans-serif;
    }
    
    .highlight-number {
        background-color: rgba(255, 159, 54, 0.2); /* Valencia Orange with opacity */
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: bold;
        color: var(--sf-accent-orange);
    }
    </style>
    """, unsafe_allow_html=True)
