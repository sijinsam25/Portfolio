import streamlit as st

# HTML code for navbar
navbar_html = """
    <nav class="navbar">
        <ul>
            <li><a href="#home">{}</a></li>
            <li><a href="#experience-summary">{}</a></li>
            <li><a href="#education">{}</a></li>
            <li><a href="#experience-highlights">{}</a></li>
        </ul>
    </nav>
"""

# Injecting CSS for the navbar
st.markdown(
    """
    <style>
    .navbar {
        background-color: #333;
        overflow: hidden;
    }
    
    .navbar ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }
    
    .navbar li {
        float: left;
    }
    
    .navbar li a {
        display: block;
        color: white;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
    }
    
    .navbar li a:hover {
        background-color: #ddd;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the navbar with Streamlit buttons
st.markdown(navbar_html.format(
    st.button("Home", key="home"),
    st.button("Experience Summary", key="experience_summary"),
    st.button("Education", key="education"),
    st.button("Experience Highlights", key="experience_highlights")
), unsafe_allow_html=True)

# Your content here
