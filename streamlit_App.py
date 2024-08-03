import streamlit as st
import pandas as pd 

import numpy as np
import pickle
import time

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages
if app_mode=='Home':    
    
    st.title("Welcome Back...")
    st.image('heart.jpeg')
    st.subheader("Are you know?")
    st.write("According to the World Health Organization (WHO), cardiovascular diseases (CVDs) are the leading cause of death globally, taking an estimated 17.9 million lives each year, which accounts for about 31% of all global deaths. Of these deaths, an estimated 85% are due to heart attacks and strokes. This translates to approximately 24,561 deaths per day from CVDs.")
    st.video("video.mp4")
    
    st.write("You can here normal heart beat of Healthy person.")
    st.audio('Heartbeat.mp3')
    st.write("")
    st.subheader("Below diagrams visualize the factots of distribution in the dataset.\n\n")
    df= pd.read_csv("heart.csv")
    
    df = pd.DataFrame(
        np.random.randn(10, 2),
        columns=['x', 'y'])
    st.line_chart(df)
    
elif app_mode == 'Prediction':


    loaded_model = pickle.load(open('heart_model.sav', 'rb'))

    def heart_prediction(input_data):
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)
        if (prediction[0] == 0):
            return 'The person is not a Heart attack patient'
        else:
            return 'The person is a Heart attack patient'

    def main():
        st.title('Heart Attack Prediction Web Application')

        age = st.text_input('Age')
        sex = st.text_input('Gender(If Male enter=1 / If Female enter=0)')
        #cp = st.text_input('Chest Pain type')
        trtbps = st.text_input('Resting Blood Pressure')
        chol = st.text_input('Cholestoral')
        fbs = st.text_input('Fasting Blood Sugar(If Yes enter =1 / If No enter=0) ')
        restecg = st.text_input('Resting Electrocardiographic Results(If Yes enter=1 / If No enter=0)')
        thalach = st.text_input('Maximum Heart Rate Achieved')
        st.slider('Maximum Heart Rate',0,200,0,)
        #exng = st.text_input('Exercise Induced Angina')
        oldpeak = st.text_input('Previous Peak')
        st.file_uploader('Upload a photo')

        #diagnosis = ''
        
        if st.button('Click to Test Result'):
            with st.spinner('Please wait...'):
                time.sleep(1)
                diagnosis = heart_prediction([age, sex, trtbps, chol, fbs, restecg, thalach, oldpeak, ])
                st.success(diagnosis)

    if __name__ == '__main__':
        main()





