# imports
import os
import sys
import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt
import streamlit as st
import awesome_streamlit as ast

sys.path.append(os.path.abspath(os.path.join('./scripts')))
from file_handler import FileHandler

def write():
    """Used to write the page in the app.py file"""
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header('Prediction on test data')
    file_handler = FileHandler()
    df = file_handler.read_csv('features/test_features.csv')
    test_df = file_handler.read_csv('src/data/test.csv')
    st.markdown('### Sample test data input')
    st.write(test_df.head(10))
    model = pickle.load(open('models/XGB Regressor_Sales 2021-08-01-16:01:09.pkl', "rb"))
    y_preds = model.predict(df)
    prediction_df = df.copy()
    prediction_df["Pred_sales"] = y_preds
    st.markdown('### Sample prediction output')
    st.write(prediction_df["Pred_sales"].head(10))
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(df)
    st.header('Feature Importance')
    plt.title('Feature importance based on SHAP values')
    shap.summary_plot(shap_values, df)
    st.pyplot(bbox_inches='tight')
    st.write('---')

    plt.title('Feature importance based on SHAP values (Bar)')
    shap.summary_plot(shap_values, df, plot_type="bar")
    st.pyplot(bbox_inches='tight')