import joblib
import streamlit as st 
import pandas as pd
import numpy as np


def main():
    machine=joblib.load('model')
    html="""
    <title>laptop_price_predictor</title>
    <body style="background-color:gray;">
    <h2 style="background-color:red;">Laptop Price Prediction</h2>
    </body>
    
    """
    st.markdown(html,unsafe_allow_html=True)
    brand=['Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI',
       'Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer',
       'Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG']
    p1=st.selectbox("enter Brand Name: ",brand)
    lap_type=['Ultrabook', 'Notebook', 'Netbook', 'Gaming', '2 in 1 Convertible',
       'Workstation']
    p2=st.selectbox("enter Laptop Type:",lap_type)
    ram=[ 8, 16,  4,  2, 12,  6, 32, 24, 64]
    p3=st.selectbox("enter Ram: ",ram)
    p4=st.number_input("enter Laptop Weight:")
    p5=st.selectbox('enter Touchscreen: ',['Yes','No'])
    p6=st.selectbox('Enter IPS Display: ',['Yes','No'])
    p7=st.number_input('Enter Screen Size: ')
    resolution=['1920x1080','1366x768','1600x900','3840x2160','2800x1800','2560x1600','2560x1440','2304x1440']
    p8=st.selectbox('Enter Screen Resolution: ',resolution)
    process=['Intel Core i5', 'Intel Core i7', 'AMD Processor', 'Intel Core i3',
       'Other Intel Processor']
    p9=st.selectbox('Enter Processor: ',process)
    p10=st.selectbox('Enter Hard Drive: ',[0,128,256,512,1024,2048])
    p11=st.selectbox('Enter SSD Size(in GBs)',[0,8,128,256,512,1024])
    p12=st.selectbox('enter Graphics Processing Unit(GPU): ',['Intel', 'AMD', 'Nvidia'])
    os=['Mac', 'Others/No OS/Linux', 'Windows']
    p13=st.selectbox('Enter Operating System: ',os)
   
    
    if st.button('Predict Price'):
        #ppi=None
        if p5=='Yes':
            p5=1
        else:
            p5=0
            
            
        if p6=='Yes':
            p6=1
        else:
            p6=0
            
        x_res=int(p8.split('x')[0])
        y_res=int(p8.split('x')[1])
        ppi=(((x_res**2)+(y_res**2))**0.5)/p7
        
        
        query=np.array([p1,p2,p3,p4,p5,p6,ppi,p9,p10,p11,p12,p13])
        query=query.reshape(1,12)
        value=np.exp(machine.predict(query))
        st.balloons()
        st.title('your predicted price:{}'.format(round(value[0],2)))
    
    
if __name__=="__main__":
    main()