import os
import streamlit as st
from PIL import Image

#____path setting

current_dict=os.path.dirname(os.path.abspath(__file__))
resume_file=os.path.join(current_dict,"assets","SijinSam_Resume_March.pdf")
css_file=os.path.join(current_dict,"style","main.css")
profile_pic=os.path.join(current_dict,"assets","profile-pic.png")


#_----general setting


PAGE_TITLE="Sijin Sam | CV"
PAGE_ICON=":computer:"
NAME=" Sijin Sam"
DESCRIPTION="""
Developer I- Software Engineering, assists in producing the GENAI product through Python development.
"""
EMAIL="sijinsam97@gmail.com"
PHONE="9495923452"

SOCIAL_MEDIA={
    "LinkedIn":"https://www.linkedin.com/in/sijin-sam-275696188",
    "GitHub":"https://github.com/sijinsam25"

}


st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

#------LOAD CSS,PDF & PROFILE PIC

with open(resume_file,"rb") as pdf_file:
    PDFbyte=pdf_file.read()

profile_pic=Image.open(profile_pic)

#--- hero section

col1,col2=st.columns(2,gap="large")

with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file,
        mime="application/octet-stream"
    )
    st.write("📧", EMAIL)
    st.write("📱",PHONE)

#----social link
    
st.write('\n')
cols=st.columns(len(SOCIAL_MEDIA))
for index,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Add CSS for fullscreen
st.markdown(
    """
    <style>
        .css-1v3fvcr {
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)
