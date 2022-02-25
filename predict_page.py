import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('Random_Forest_Model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model
        

data = load_model()

regressor = data["model"]
MainBranch_encode = data["MainBranch_encoder"]
Employment_encode = data["Employment_encoder"]
Country_encode = data["Country_encoder"]
EdLevel_encode = data["EdLevel_encoder"]
Age1st_encode = data["Age1st_encoder"]
OrgSize_encode = data["OrgSize_encoder"]
Age_encode = data["Age_encoder"]


def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some informatuion to predict the salary""")


    countries = (
        'Sweden', 'Spain', 'Germany', 'Turkey', 'Canada', 'Singapore',
        'France', 'Switzerland',
        'United Kingdom of Great Britain and Northern Ireland',
        'Russian Federation', 'Israel', 'Ukraine',
        'United States of America', 'Brazil', 'Bulgaria', 'Greece',
        'Italy', 'Netherlands', 'Poland', 'Hungary', 'Pakistan', 'Nigeria',
        'Other', 'Bangladesh', 'Austria', 'Viet Nam', 'Romania',
        'Sri Lanka', 'India', 'Lithuania', 'Slovenia', 'Croatia',
        'Denmark', 'Ireland', 'Egypt', 'Colombia', 'Australia', 'Belgium',
        'Chile', 'Indonesia', 'Iran, Islamic Republic of...', 'Portugal',
        'Slovakia', 'Finland', 'Argentina', 'Japan', 'South Africa',
        'Norway', 'Serbia', 'Malaysia', 'Czech Republic', 'Kenya',
        'Uruguay', 'China', 'Mexico', 'Taiwan', 'Nepal', 'Philippines',
        'New Zealand'
    )

    mainbranch = (
        'I am a developer by profession',
       'I am not primarily a developer, but I write code sometimes as part of my work'
    )

    edlevel = (
        "Master's degree", "Bachelor's degree", 'Post grad',
       "WAEC/NECO and it's equivalent worldwide"
    )

    age1stcode = (
        '11 - 17 years', '5 - 10 years', '25 - 34 years', '18 - 24 years',
       '35 - 44 years', 'Younger than 5 years', '45 - 54 years',
       '55 - 64 years', 'Older than 64 years'
    )

    orgsize = (
        '10 to 19 employees', '1,000 to 4,999 employees',
       '100 to 499 employees', '500 to 999 employees',
       '5,000 to 9,999 employees', '2 to 9 employees',
       '20 to 99 employees', '10,000 or more employees',
       'Just me - I am a freelancer, sole proprietor, etc.',
       "I don't know"
    )

    education = (
        "Master's degree", "Bachelor's degree", 'Post grad',
        "WAEC/NECO and it's equivalent worldwide"
    )

    age = (
        '25-34 years old', '45-54 years old', '35-44 years old',
       '18-24 years old', '55-64 years old', '65 years or older',
       'Under 18 years old', 'Prefer not to say'
    )


    employment = (
    'Employed full-time', 'I prefer not to say',
       'Independent contractor, freelancer, or self-employed',
       'Employed part-time', 'Retired'
    )

    MainBranch = st.selectbox("Category", mainbranch)
    Employment = st.selectbox("Employment State", employment)
    Country = st.selectbox("Country", countries)
    Education = st.selectbox("Education Level", education)
    Age1stCode = st.selectbox("Age you first coded", age1stcode)
    OrgSize = st.selectbox("Organization Size", orgsize)
    Age = st.selectbox("Age", age)

    YearsCode = st.slider("Num of years coded", min_value=0.5, max_value=50., value=5.)
    YearsCodePro = st.slider("Num of years coded professionally", min_value=0.5, max_value=50., value=5.)   


    input = st.button("Calculate Salary")

    if input:
        input = np.array([[MainBranch, Employment, Country, Education, Age1stCode, YearsCode, YearsCodePro, OrgSize, Age]])
        input[:, 0] = MainBranch_encode.transform( input[:, 0])
        input[:, 1] = Employment_encode.transform( input[:, 1])
        input[:, 2] = Country_encode.transform( input[:, 2])
        input[:, 3] = EdLevel_encode.transform( input[:, 3])
        input[:, 4] = Age1st_encode.transform(input[:, 4])
        input[:, 7] = OrgSize_encode.transform(input[:, 7])
        input[:, 8] = Age_encode.transform(input[:, 8])
        input = input.astype(float)

        salary = regressor.predict(input)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")