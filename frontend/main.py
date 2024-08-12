import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Predict", page_icon="🔮", layout="wide")

# Set page title
st.title("Predict Churn")

# Function for selecting models
def select_model():
    col1, col2 = st.columns(2)
    with col1:
        choice = st.selectbox('Select a model', options=['LGBM', 'XGBClassifier', 'RandomForest'], key='select_model')
    with col2:
        pass
    return choice

# Function for making prediction
def make_prediction(): 
    selected_model = st.session_state['select_model']
    Region = st.session_state['Region']
    Tenure = st.session_state['Tenure']
    Recharge_Amount = st.session_state['Recharge_Amount']
    FREQUENCE_RECH = st.session_state['Recharge_Frequency']
    REVENUE = st.session_state['Revenue']
    ARPU_SEGMENT = st.session_state['ARPU_Segment']
    FREQUENCE = st.session_state['Income_Frequency']
    DATA_VOLUME = st.session_state['Data_Volume']
    ON_NET = st.session_state['On_Net']
    ORANGE = st.session_state['Orange']
    TIGO = st.session_state['Tigo']
    REGULARITY = st.session_state['Regularity']
    TOP_PACK = st.session_state['Top_Pack']
    FREQ_TOP_PACK = st.session_state['Freq_Top_Pack']

    base_url = 'http://127.0.0.1:8000/'
    endpoint = 'LGBM' if selected_model == 'LGBM' else 'XGBClassifier'
    url = base_url + endpoint

    data = {
        'REGION': Region, 
        'Tenure': Tenure, 
        'Recharge_Amount': Recharge_Amount, 
        'FREQUENCE_RECH': FREQUENCE_RECH, 
        'REVENUE': REVENUE, 
        'ARPU_SEGMENT': ARPU_SEGMENT, 
        'FREQUENCE': FREQUENCE, 
        'DATA_VOLUME': DATA_VOLUME, 
        'ON_NET': ON_NET, 
        'ORANGE': ORANGE, 
        'TIGO': TIGO, 
        'REGULARITY': REGULARITY, 
        'TOP_PACK': TOP_PACK, 
        'FREQ_TOP_PACK': FREQ_TOP_PACK
    }
    
    # Send POST request with JSON data using the json parameter
    response_status = requests.get(base_url)

    if response_status.status_code == 200:
        response = requests.post(url, json=data, timeout=30)
        if response.status_code == 200:
            pred_prob = response.json()
            prediction = pred_prob['prediction']
            probability = pred_prob['probability']

            st.session_state['prediction'] = prediction
            st.session_state['probability'] = probability
        else:
            st.write('Error in prediction response from server.')
    else:
        st.write('Unable to connect to the server.')

# Creating the form
def display_form():
    select_model()

    with st.form('input_features'):
        col1, col2 = st.columns(2)
        with col1:
            st.write('### Customer Information')
            st.text_input('Region', key='Region')
            st.number_input('Tenure (months)', min_value=0, step=1, key='Tenure')
            st.number_input('Recharge Amount', min_value=0.0, format="%.2f", step=1.00, key='Recharge_Amount')
            st.number_input('Recharge Frequency', min_value=0.0, format="%.2f", step=1.00, key='Recharge_Frequency')
            st.number_input('Revenue', min_value=0.0, format="%.2f", step=1.00, key='Revenue')
            st.text_input('ARPU Segment', key='ARPU_Segment')
            st.number_input('Income Frequency', min_value=0.0, format="%.2f", step=1.00, key='Income_Frequency')
            st.number_input('Data Volume', min_value=0.0, format="%.2f", step=1.00, key='Data_Volume')

        with col2:
            st.write('### Network Information')
            st.number_input('On Net', min_value=0.0, format="%.2f", step=1.00, key='On_Net')
            st.number_input('Orange', min_value=0.0, format="%.2f", step=1.00, key='Orange')
            st.number_input('Tigo', min_value=0.0, format="%.2f", step=1.00, key='Tigo')
            st.number_input('Regularity', min_value=0.0, format="%.2f", step=1.00, key='Regularity')
            st.text_input('Top Pack', key='Top_Pack')
            st.number_input('Frequency of Top Pack', min_value=0.0, format="%.2f", step=1.00, key='Freq_Top_Pack')

        st.form_submit_button('Submit', on_click=make_prediction)

if __name__ == '__main__':
    display_form()

    final_prediction = st.session_state.get('prediction')
    final_probability = st.session_state.get('probability')

    if final_prediction is None:
        st.write('Predictions show here!')
        st.divider()
    else:
        if final_prediction.lower() == 'yes':
            st.markdown(f'### Customer is likely to churn😞.')
            st.markdown(f'## Probability: {final_probability:.2f}%')
        else:
            st.markdown(f'### Customer is unlikely to churn😊.')
            st.markdown(f'## Probability: {final_probability:.2f}%')
