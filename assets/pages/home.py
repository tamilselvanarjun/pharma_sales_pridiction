# imports
import streamlit as st
import awesome_streamlit as ast


def write():
    """Used to write the page in the run_app.py file"""
    st.title('Rossmann Pharmaceuticals Pridiction Dashboard')
    st.write('\n\n\n\n')
    st.image("./assets/src/home.jpg")
    st.write('---')
    st.write(
        """
        The data scientists at Rossmann Pharmaceuticals have collected three years of sales 
        data for different  products across four stores in different location. 
        Also, certain statistics attributes of sales on each store have been defined. 
        The aim is to build a predictive model and predict 
        sales of all their stores across several cities six weeks ahead of time.
        """
    )