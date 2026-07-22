import streamlit as st
import pickle

with open("emotion.pkl","rb+") as file:
    model = pickle.load(file)

with open("vector.pkl","rb+") as file:
    vector = pickle.load(file)

encoder={0:'anger',
         1:'disgust',
         2:'fear',
         3:'joy',
         4:'love',
         5:'neural',
         6:'sadness',
         7:'surprice'}

st.header("Emotion text Classification")
text = st.text_area("Enter the text")
bn = st.button("Click Here")
if bn and text:
    result = model.predict(vector.transform(list(text)))
    st.text(text)
   



