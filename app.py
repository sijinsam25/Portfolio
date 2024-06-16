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

with open(css_file) as file:
    st.markdown("<style>{}</style>".format(file.read()),unsafe_allow_html=True)


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


#----experience & qualifications
    
st.write('\n')
st.subheader("Experience Summary")
st.write(
    """
- ✔️ Having 2.5+ years’ experience in Software Development in IT industry. 
- ✔️ Actively involved in Generative AI, utilizing Python to contribute to innovative projects 
      in AI-driven testing and automation. 
- ✔️ Good knowledge on Data Science, Machine Learning Fundamentals.
- ✔️ Have hands-on experience with Machine Learning Project and Python Development. 
- ✔️ Proficient analytical skills honed through practical application.  
- ✔️  Gained Experience in Data Preparation, Exploratory Data Analysis, Data Visualization
- ✔️ Gained Domain Knowledge in Automation testing and Manual Testing. 
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Proficient in Python. 
- 📊 Basic understanding of Data Science, Machine Learning, Django, Flask, Restful API, 
      AWS Dynamo DB, GitHub, and Kaggle. 
- 📚 Strong analytical skills. 
- 🗄️ Experienced with development IDEs including Jupyter Notebook, Spyder, PyCharm, 
      and Visual Studio Code.
"""
)


#----EXPERIENCE HIGHLIGHTS

st.write('\n')
st.subheader("EXPERIENCE HIGHLIGHTS")
st.write("---")


#job1
st.write('\n')
st.write("🚧", "**Developer I- Software Engineering | UST Trivandrum**")
st.write("July 2021 - Present")
st.write(
    """
- Role: Developing, implementing, and refining AI models for generating test cases, data, or scenarios in software testing.
- Tools: Python, IDE Visual Studio Code.
- Models: GPT-3.5, Azure OPEN AI GPT-4.
- Specialization: NLP automation, focusing on text extraction and Named Entity Recognition (NER).
- Libraries: Numpy, Pandas, PyMupdf, python-docx, Spacy, NLTK, LLM, OpenAI.
- Previous project: Experimented with transformer architectures like BERT and GPT to enhance NLP automation.
- Contributions: Streamlined automation processes, improved efficiency in handling unstructured text data.
- Collaboration: Worked with cross-functional teams to understand testing requirements.
- Research: Contributed to ongoing R&D efforts to advance Generative AI capabilities in testing domain.
"""
)

# job2
st.write('\n')
st.write("🚧", "**Software Intern| Zlight INC. KOCHI**")
st.write("August 2020 - January 2021")
st.write(
    """
- Project: Development of an eCommerce website using Python in the backend.
- Framework: Utilized Django for backend development.
- API: Implemented Restful API for smooth interaction between frontend and backend.
- Database: Managed data using DynamoDB on AWS.
- Deployment: Deployed on AWS domain using EC2 instance.
- Storage: Used S3 bucket for storing static files and media.
- IDE: Visual Studio Code for development.
- Technologies: Python, Django Framework, Restful API, AWS services (EC2, S3, DynamoDB).
"""
)

#job 3
st.write('\n')
st.write("🚧", "**Data Science Intern| INNODATATICS INC. KOCHI**")
st.write("Febuary 2020 - April 2020")
st.write(
    """
- Project: Machine Learning prediction project.
- Workflow: Followed Data Science pipeline.
- Technologies: Python for programming.
- Libraries: Numpy, Pandas, Matplotlib, Seaborn, Scikit-learn.
- IDEs: Jupyter Notebook, Spyder, Google Colab.
- Steps: Data collection, cleansing, EDA, visualization, imputation, feature engineering, data splitting, scaling, applying ML algorithms (Logistic Regression, Decision Tree, Random Forest, KNN, Naïve Bayes, SVM), deployment.
""")

# --- Certification ---
st.write('\n')
st.subheader("Certification")
st.write(
    """
- ✔️ Certification in Data Science with Python and R from ExcelR Solutions 
"""
)

# --- Education ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- **B.Tech in Electronics and Communication Engineering (ECE)**
-   ✔️Mangalam College of Engineering, Kottayam
-   ✔️Dr. APJ Abdul Kalam Technical University (KTU)
-   ✔️Graduated: 2019
-   ✔️CGPA: 7.84
"""
)







