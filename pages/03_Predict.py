import streamlit as st
import pandas as pd
import joblib
import os
import pickle

# Set page configuration
st.set_page_config(
    page_title='Customer Churn Predict Page',
    layout='wide'
)

# Load models
@st.cache_resource(show_spinner='Models Loading')
def load_rf():
    return joblib.load('Models/RandomForest_pipeline.joblib')

def select_model():
    # Create a selectbox for model selection
    model_name = st.selectbox('Select Model', options=['Random Forest'], key='selected_model')

    # Load the corresponding model based on the selection
    if model_name == 'Random Forest':
        return load_rf()
    else:
        st.warning("Please select a valid model.")
        return None

def make_prediction(pipeline):
    data = {
        'MONTANT': st.session_state['MONTANT'], 'FREQUENCE_RECH': st.session_state['FREQUENCE_RECH'], 
        'REVENUE': st.session_state['REVENUE'], 'ARPU_SEGMENT': st.session_state['ARPU_SEGMENT'], 
        'FREQUENCE': st.session_state['FREQUENCE'], 'DATA_VOLUME': st.session_state['DATA_VOLUME'], 
        'ON_NET': st.session_state['ON_NET'], 'ORANGE': st.session_state['ORANGE'], 
        'TIGO': st.session_state['TIGO'], 'REGULARITY': st.session_state['REGULARITY'], 
        'FREQ_TOP_PACK': st.session_state['FREQ_TOP_PACK'],'REGION': st.session_state['REGION'],'TENURE': st.session_state['TENURE'], 
        'TOP_PACK': st.session_state['TOP_PACK']
    }

    df = pd.DataFrame([data])
    prediction = pipeline.predict(df)
    
    st.session_state['prediction'] = prediction

    # Save results
    df['prediction'] = prediction
    df['model_used'] = st.session_state['selected_model']

    history_file_path = 'data/history.csv'
    df.to_csv(history_file_path, mode='a', header=not os.path.exists(history_file_path), index=False)

    return prediction
if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None

def display_form():
    pipeline = select_model()
    with st.form('input_form'):
        st.markdown('### Customer Details')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.number_input('Top-up Amount', min_value=0, max_value=1000000, key='MONTANT')
            st.number_input('Number of Times the Customer Refilled', min_value=0, max_value=100, key='FREQUENCE_RECH')
            st.number_input('Monthly Income of the Client', min_value=0, max_value=1000000, key='REVENUE')
            st.number_input('Income over 90 Days / 3', min_value=0, max_value=100000, key='ARPU_SEGMENT')
            st.number_input('Number of Times the Client has Made an Income', min_value=0, max_value=100000, key='FREQUENCE')
            st.number_input('Number of Connections', min_value=0, max_value=100000, key='DATA_VOLUME')
        with col2:
            st.number_input('Inter Expresso Call', min_value=0, max_value=100000, key='ON_NET')
            st.number_input('Call to Orange', min_value=0, max_value=100000, key='ORANGE')
            st.number_input('Call to Tigo', min_value=0, max_value=100000, key='TIGO')
        with col3:
            st.number_input('Number of Times the Client is Active for 90 Days', min_value=0, max_value=100, key='REGULARITY')
            st.number_input('Number of Times the Client has Activated the Top Packs', min_value=0, max_value=100, key='FREQ_TOP_PACK')
            st.selectbox('Location of Each Client', ['DAKAR','SAINT-LOUIS', 'THIES', 'LOUGA', 'MATAM', 'FATICK', 'KAOLACK','DIOURBEL', 'TAMBACOUNDA', 'ZIGUINCHOR', 'KOLDA', 'KAFFRINE', 'SEDHIOU','KEDOUGOU'], key='REGION')
            st.selectbox('Duration in the Network', ['Short-term', 'Mid-term', 'Medium-term', 'Very short-term'], key='TENURE')
            st.selectbox('contract', ['data', 'international', 'messaging', 'social_media','value_added_services', 'voice'], key='TOP_PACK')
        st.form_submit_button('Predict Churn', on_click=make_prediction, kwargs=dict(pipeline=pipeline))
        
if __name__ == '__main__':
	        display_form() 

