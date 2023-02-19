import streamlit as st

# Set page configuration
st.set_page_config(page_title="Data Analyst Resume", page_icon=":pencil:", layout="centered")

# Set page background color and text color
st.markdown(
    """
    <style>
    body {
        color: white;
        background-color: #121212;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define the main function
def main():
    # Set the title
    st.title("Rushikesh Kawade")
    st.markdown("<hr>", unsafe_allow_html=True)

    # Add a brief description
    st.write("I am a data analyst with experience in data analysis, data visualization. I am proficient in Python and SQL. My goal is to help organizations make data-driven decisions by providing meaningful insights from their data.")

    # Add an education section
    st.header("Education")
    st.subheader("Bachelor of Technology - BTech, Electrical engineering")
    st.write("Rajarambapu Institute of Technology, Rajaramnagar, SAKHARALE, Nov 2020")
    st.write("CGPA: 7.54")

    # Add a work experience section
    st.header("Work Experience")
    st.subheader("Data Analyst")
    st.write("ABC Company, January 2019 - Present")
    st.write("- Perform data analysis on large datasets to identify trends and patterns.")
    st.write("- Develop and maintain Tableau dashboards to visualize key metrics.")
    st.write("- Work with cross-functional teams to support data-driven decision making.")
    st.subheader("Data Analyst Intern")
    st.write("XYZ Company, May 2018 - December 2018")
    st.write("- Assisted in data cleaning, transformation, and analysis.")
    st.write("- Created visualizations and presentations to communicate findings to stakeholders.")

    # Add a technical skills section
    st.header("Technical Skills")
    st.write("- Python")
    st.write("- SQL")
    st.write("- Pandas")
    st.write("- NumPy")

    # Add a projects section
    st.header("Projects")
    st.subheader("Customer Segmentation Analysis")
    st.write("- Performed exploratory data analysis on customer purchase history data.")
    st.write("- Conducted customer segmentation using K-means clustering algorithm.")
    st.write("- Visualized the results using a Tableau dashboard.")
    st.subheader("Employee Attrition Prediction")
    st.write("- Built a logistic regression model to predict employee attrition.")
    st.write("- Evaluated the model's performance using confusion matrix and ROC curve.")
    st.write("- Communicated the results to HR department using a PowerPoint presentation.")

    # st.write("---")
    # st.markdown("<br>", unsafe_allow_html=True)
    # Add a contact information section
    st.header("Contact Information")
    st.write("- Email: rushikawade45@gmail.com")
    st.write("- LinkedIn: www.linkedin.com/in/rushikesh-kawade-84770020a")
    st.markdown("<br>", unsafe_allow_html=True)

    # st.write("Thank you for taking the time to review my resume. I am excited about the opportunity to contribute my skills and experience to your organization.")
    # st.write("Best regards,")
    # st.write("John Doe")

# Call the main function
if __name__ == '__main__':
    main()
