# imports
import streamlit as st
import pandas as pd


def write():
    """Used to write the page in the app.py file"""
    st.title('Data description')
    st.write("""
    Most of the data fields are easy to understand, but just to highlight some of the features present:
    *Store, Date, Sales, Customers, Open, State Holiday, School Holiday, Store Type, Assortment, Competition and Promotion.*
    The *Store Type, Assortment, Competition* and *Promotion* features are store tailored.
    The *Sales, Customers, Open, State Holiday* and *School Holiday* features vary across the stores with days.
    """)
    na_value=['',' ','nan','Nan','NaN','na', '<Na>']
    train = pd.read_csv('src/data/train.csv', na_values=na_value)
    store = pd.read_csv('src/data/store.csv', na_values=na_value)
    full_train = pd.merge(left = train, right = store, how = 'inner', left_on = 'Store', right_on = 'Store')
    full_train = full_train.set_index('Store')
    st.write('---')
    st.write('Sample stores data')
    st.write(store.head(20))
    st.write('---')
    st.write('Sample historical data including Sales and Customers')
    st.write(train.sample(20))
    st.write('---')
    st.write('Sample training data containing the input features')
    st.write(full_train.sample(20))