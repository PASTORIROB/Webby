from pathlib import Path
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "testrp.jpg"
#grad_pic = current_dir / "assets" / "grad.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Roberts Pastori Digital Resume"
PAGE_ICON = ":wave:"
NAME = "Robert Pastori"
DESCRIPTION = """
Senior Analyst, assisting institutional trading operations by creating and maintaining automated reports/databases.
"""
EMAIL = "PastoriRob@gmail.com"
SOCIAL_MEDIA = {
   
    "🛠️ LinkedIn": "https://www.linkedin.com/in/rpastori1989/",
    "👨‍💻 GitHub": "https://github.com/PASTORIROB",   
   
    
}


PROJECTS = {
    "🏆 FINRA Series 7": "https://brokercheck.finra.org/individual/summary/6603334",
    "👨‍🎓 MBA from University of Central Florida": "https://UCF.EDU",
    "👨‍🎓 Finance BS from University of Central Florida": "https://UCF.EDU",
   
    
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 11 Years of experience in Trading Operations and Finance
- ✔️ Strong hands-on coding experience with Python and VBA using MS Excel/Access
- ✔️ Great understanding of data structures and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python , SQL, VBA, Typescript
- 📊 Data Visualization: PowerBi, MS Excel, Plotly
- 🗄️ Databases: Oracle, MySQL, MS Access, SQLite
"""
)
#- 📚 Modeling: Logistic regression, linear regression, decition trees

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Business Technical Liaison Senior Analyst | BNY Mellon – Pershing**")
st.write("03/2022 - Present")
st.write(
    """
- ►  Developed a daily automation that verified incoming vendor data by reconciling internal and external trade data to ensure the vendor correctly reported fees, saving the firm hundreds of thousands of dollars over time.
- ►  I serve as the in-house MS Excel expert for all of Pershing Trading Services, capable of building macros or creating custom pivot tables to effectively present metrics from complex financial instruments.
- ►  Used Python scripting to monitor daily automated reports on a loop that notified the team if something went wrong with any report.
- ►  I effectively communicated with non-tech-savvy stakeholders by using flowcharts and diagrams, ensuring a more efficient and error-free product development process.
- ►  Constructed ad-hoc reports for Directors using various tools such as SQL, Python and Pandas involving complex financial products.
- ►  Developed UiPath Studio Pro robots that have yielded hundreds of hours of time savings for the firm and nearly eliminated the risk of data entry errors.
- ►  Constructed business metrics and visualisations from raw trade data pulled from multiple Oracle databases.
- ►  Collaborated with stakeholders to create solutions to time sensitive regulatory and compliance issues. 
- ►  Created Power Automate flows that automated tedious tasks using TypeScript code within M365 Excel scripts.

"""
)


# --- JOB 2
st.write('\n')
st.write("🚧", " Operations Analyst | Cowen Inc.")
st.write("04/2017 - 03/2022")
st.write(
    """
- ► Programmed and automated a daily dashboard for the Managing Director and Chief Operating Officer, giving a clear view of breaks across the firm and how they are resolved.
- ► Managed a global team of analysts responsible for reconciling hundreds of accounts, directly accountable for flaws if found by auditors.
- ► Routinely trusted to use critical thinking while programming Excel VBA code, transforming data into a loadable format and eliminating errors for teams, reducing risks.
- ►Led quarterly and yearly presentations of our reporting procedures and results to external and internal auditors.

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Operations Associate | Convergex Execution Services**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Reconciled cash and stock accounts in over 50 markets with different currencies, unwindings complex trades to balance the books.
- ► Wrote simple macros to improve productivity.
- ► Compiled, stored, and audited large amounts of trading data.
"""
)




# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

# Create the Matplotlib chart
plt.plot(x, y)
plt.xlabel('Hard Work')
plt.ylabel('Reward')
plt.title('Robs Career Trajectory')
st.pyplot(plt)
