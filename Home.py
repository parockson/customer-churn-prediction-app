import streamlit as st
import yaml
from yaml.loader import  SafeLoader
import streamlit_authenticator as stauth

# Set up Home page
st.set_page_config(
    page_title="Customer Churn App",
    layout="wide"
)


    # Create two columns
col1, col2 = st.columns(2)

with col1:
        #st.write("Predict if a customer is about to churn based on known characteristics using Machine Learning.")
        
        #st.write("**About us**")
        st.write("Kryton consultancy is a team of Data scientist with a combined experience of 10 years."
             "We build applications for industries that are interested in seeing continouos improvement and value creation by identifying areas of growth and reducing wastage")
        st.write("### Key Features",)
        st.write("""
        - **Data**: Access the data.
        - **Dashboard**: Explore interactive data visualizations for insghts.
        - **Predict**: See predictions for customer churn.
        - **History**: See past predictions.

        """)
        
        st.write("### Machine Learning Integration",)
        st.write("""
                - **Accurate Predictions**: Integrate advanced ML algorithms for accurate predictions.
                - **Data-Driven Decisions**: Leverage comprehensive customer data to inform strategic initiatives.
                - **Variety**: Choose between two advanced ML algorithms for predictions""")

with col2:
        st.write("### Follow the instructions below on how to run application")
        st.code("""
          activate virtual environment
          ./venv/scripts/activate
          streamlit run Home.py
    """)
        st.write("### User Benefits",)
        st.write("""
        - **Accurate Prediction**: Reduce churn rate.
        - **Data-Driven Decisions**: Inform strategic initiatives.
        - **Enhanced Insights**: Understand customer behavior.
        """)
        
        with st.expander("Need Help?", expanded=False):
            st.write("""
                     Additional Information for Logged-in Users""
            """)
        
        st.link_button('Repository on Github', url='https://github.com/parockson/customer-churn-prediction-app')