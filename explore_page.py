from lib2to3.pgen2.pgen import DFAState
from isort import file
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#function groups countries
def shorten_categories (categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] ='Other'
    return categorical_map

def convert_to_number(x):
    if x == 'More than 50 years':
        return 50
    elif x == 'Less than 1 year':
        return 0.5
    else:
        return float(x)


def education_group(x):
    if ("Bachelor" in x):
        return "Bachelor's degree"
    elif ("Master" in x):
        return "Master's degree"
    elif ("Professional degree" in x) or ("Other doctoral" in x):
        return "Post grad"
    else:
        return "WAEC/NECO and it's equivalent worldwide"

@st.cache
def load_data():
    file = pd.read_csv('survey_results_public.csv')
    loaded_data = file[['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedCompYearly']]
    loaded_data = loaded_data.rename({'ConvertedCompYearly': 'Salary'}, axis = 1)
    loaded_data = loaded_data[loaded_data.Salary.notnull()]
    loaded_data = loaded_data.dropna()

    country_map = shorten_categories(loaded_data.Country.value_counts(), 100)
    loaded_data.Country = loaded_data.Country.map(country_map)
    loaded_data = loaded_data[loaded_data.Salary <= 250000]

    loaded_data.YearsCodePro = loaded_data.YearsCodePro.apply(convert_to_number)
    loaded_data.EdLevel = loaded_data.EdLevel.apply(education_group)
    return loaded_data
    
import_data = load_data()

def show_explore_page():
    st.title("Explore Software Enigineer Salaries")

    st.write(
        """
        ### Stack Overflow Developer Survey 2021
        """
    )

    df = import_data.Country.value_counts()

    st.markdown('<iframe title="Stack Overflow Software Developer Salary - Sala" width="1010" height="700" src="https://app.powerbi.com/view?r=eyJrIjoiYjNjYTc2ODMtZGU1Yi00ZmNjLTkxOTctZGQyZjU0NDg4ZTI4IiwidCI6IjkxODhmNzhlLWI4NDUtNGRmYy04ZDIxLTlhM2M1M2FjZjg3ZiJ9" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(df, labels=df.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")

    st.write("""### Number of Data from different countries""")

    st.pyplot(fig1)

    st.write(
        """
        #Mean Salary Based on Country
        """
    )

    df = import_data.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(df)

    st.write(
        """
        #Mean Salary Based on Experience
        """
    )

    df = import_data.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(df)
