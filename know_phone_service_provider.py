import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import streamlit
streamlit.set_page_config(page_title="Know Phone Service Provider and Country", page_icon="Capture.JPG")
streamlit.image("Capture.JPG")
def true():

    streamlit.subheader("Know you service provider and which country")
    a = streamlit.text_input("Enter your phone number: ",
                             placeholder="Please Enter your input with countrycode eg+91-9087")
    button = streamlit.button("Press it")

    if button:
        try:
            phone = phonenumbers.parse(a)
            b = (carrier.name_for_number(phone, "en"))
            c = (geocoder.country_name_for_number(phone, "en"))
            streamlit.text(f"Service Provider - {b}")
            streamlit.text(f"Country-  {c}")
        except Exception as e:
            streamlit.text("You entered wrong data. For mor information contact - +917892293254")
def hci():
    streamlit.video("SP.mp4")
z = streamlit.sidebar.radio("Go To",("Know Service Provider", "How to check it"))
if z == "Know Service Provider":
    true()

if z == "How to check it":
    hci()







