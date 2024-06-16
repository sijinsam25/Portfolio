import streamlit as st

# Define the content for the experience summary
experience_summary_content = """
- ✔️ Having 2.5+ years’ experience in Software Development in IT industry.
- ✔️ Actively involved in Generative AI, utilizing Python to contribute to innovative projects 
      in AI-driven testing and automation.
- ✔️ Good knowledge of Data Science, Machine Learning Fundamentals.
- ✔️ Hands-on experience with Machine Learning Project and Python Development.
- ✔️ Proficient analytical skills honed through practical application.
- ✔️ Gained Experience in Data Preparation, Exploratory Data Analysis, Data Visualization.
- ✔️ Gained Domain Knowledge in Automation testing and Manual Testing.
"""

# HTML code for navbar
navbar_html = """
    <nav class="navbar">
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#experience-summary">{}</a></li>
            <li><a href="#education">Education</a></li>
            <li><a href="#experience-highlights">Experience Highlights</a></li>
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

# Handle button clicks
if st.session_state.home:
    # Handle home button click
    pass
elif st.session_state.experience_summary:
    # Handle experience summary button click
    with st.expander("Experience Summary"):
        st.markdown(experience_summary_content)

# Your content here
