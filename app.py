import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

logo = st.sidebar.image('Stack Overflow.png')
page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
    
description = st.sidebar.markdown('Data used in building the machine learning model is the cleaned results of the 2021 Stack Overflow Developer Survey.  \nThe survey was fielded  from May 25 2021, to June 15 2021.  \nThe median time spent on the survey for qualified responses was 10.21 minutes.  \nRespondents were recruited primarily through channels owned by Stack Overflow.  \nYou can find the official published results here:  \nhttps://insights.stackoverflow.com/survey/2021')
