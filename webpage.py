import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import smtplib
import os
from streamlit_lottie import st_lottie
UserMail = os.getenv('UserMail')
UserPass = os.getenv('UserPass')

import time


def load_lottie(url):
    r =requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_Coding =load_lottie( "https://assets2.lottiefiles.com/packages/lf20_57TxAX.json"
)
df = pd.read_csv('D:\Downloads\pokemon_data.csv')
dic = {
    "Name":"Ronak",
    "City":"Pali",
    "State":"Rajasthan",
    "Country":"India"
}
# plt.scatter(df["Attack"],df["Defense"])
# st.pyplot()
st.set_page_config(page_title="webpage", page_icon=":dollar:", layout="wide")
st.title("Weird webpage")
st.write("---")
st.write(" ### Welcome to my weird webpage, I hope you enjoy :smiling_imp:")
st.dataframe(df)
st.json(dic)
st.write(dic)
data = df.iloc[:,4:6]
st.line_chart(data)
if st.button("::blue_heart::"):
    st.write("thank you")
temp = st.text_input(" ")
st.write( temp + "thank you")
if st.button("Camera"):
    st.camera_input("camera")
    if st.button("close"):
        st.camera_input("close")
if st.checkbox("you agree"):
    st.button('submit')
st_lottie(lottie_Coding,height=500,width=500)

def notifyme(mail):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(UserMail,UserPass)
        Subject = "Price drop!!!"
        Body = "There is a price drop on the amazon product you have been looking for"
        msg = f"Subject:{Subject} \n\n {Body}"
        ReciverMail =mail
        smtp.sendmail(UserMail,ReciverMail,msg)

def PriceCheck(url):
    header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}
    r = requests.get(url,headers=header)
    s = BeautifulSoup(r.content,'html.parser')
    ans = s.find(class_ = "a-offscreen").get_text()
    ans = ans[1:]
    ans = float(ans)
    return ans


URL = st.text_input("URL")
key = st.number_input('Key')
key = float(key)
mail = st.text_input("mail")
if st.button("check"):
    st.write(PriceCheck(URL))
    ans = PriceCheck(URL)
    a = True
    while(a):
        if ans<key:
            notifyme(mail)
            time.sleep(100)




