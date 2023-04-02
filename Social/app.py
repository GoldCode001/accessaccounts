from PIL import Image
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Access your social media accounts", page_icon=":smile:", layout="wide")
st.title("Access.com")
st.subheader("Gain access to your Social media accounts in seconds")
st.sidebar.success("select a page")
left_column, right_column= st.columns(2)


def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
#use local css
def local_css(file_name):
    with open(file_name)as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles/style.css")
#load asset
lottie_coding=load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_T4XJOLEPj5.json")

instagram = Image.open("Images\instagram.png")

#----Login to your facebook account----
with st.container():
    st.write("---")
    st.subheader("Login to your Facebook account")
    st.write("Click the link below to login to your Facebook account")
    st.write("[Login >](https://www.facebook.com/login/)")

#----Login to your Whatsapp account----
with st.container():
    st.write("---")
    st.subheader("Login to your Whatsapp account")
    st.write("Click the link below to login to your Whatsapp account to start messaging")
    st.write("[Login >](https://web.whatsapp.com/login/)")

#----Login to your Instagram account----
with st.container():
    st.write("---")
    st.subheader("Login to your Instagram account")
    st.write("Click the link below to login to your Instagram account")
    st.write("[Login >](https://www.instagram.com/login/)")

#----Login to your Quora account----
with st.container():
    st.write("---")
    st.subheader("Login to your Quora account")
    st.write("Click the link below to login to your Quora account")
    st.write("[Login >](https://www.quora.com/login/)")

#----Login to your Linked in account----
with st.container():
    st.write("---")
    st.subheader("Login to your LinkedIn account")
    st.write("Click the link below to login to your LinkedIn account")
    st.write("[Login >](https://www.LinkedIn.com/login/)")

#contact form
with st.container():
    st.write("---")
    st.header("Give us feedback, we'd appreciate..")
    st.write("##")

    #https://formsubmit.co
    contact_form="""
    <form action="https://formsubmit.co/goldcod3@gmail.com" method="POST">
        <input type="hidden" name="_captcha value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_coding, height=400, key='coding')

