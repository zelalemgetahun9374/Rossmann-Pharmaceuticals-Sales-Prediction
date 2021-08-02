# imports
import streamlit as st
import awesome_streamlit as ast


def write():
    """Used to write the page in the app.py file"""
    st.title('Rossmann Pharmaceuticals')
    st.write('\n\n\n\n')
    st.image("./src/images/rosssman.jpg")
    st.write('---')
    st.write(
        """
        Rossmann pharmaceuticals is an international pharamaceutical company that operates over 3,000 drug stores in 7 European countries.
        Currently, the finance team in Rossmann is concerned with predicting their daily sales for up to six weeks in advance.
        """
    )