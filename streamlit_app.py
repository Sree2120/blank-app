import streamlit as st
import requests

st.title("Currency Converter")
st.header("I finally did it!")
st.subheader("Convert your currency..")

choice1=st.number_input("Enter ", min_value=0.0, step=0.10)
choice2=st.selectbox("Select the currency you want to convert from", ["USD", "EUR", "GBP", "INR", "JPY"])
choice3=st.selectbox("Select the currency you want to convert to", ["USD", "EUR", "GBP", "INR", "JPY"])
if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/{choice2}"
    response = requests.get(url)
    data = response.json()
    
    if choice3 in data['rates']:
        conversion_rate = data['rates'][choice3]
        converted_amount = choice1 * conversion_rate
        st.success(f"Answer is : {converted_amount:.2f} {choice3}")
    else:
        st.error("Invalid currency selected for conversion.")
else:

    st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)." 
    )
