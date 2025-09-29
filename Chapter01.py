import streamlit as st

st.title("Savitribai Phule Pune University")
st.subheader("Department of Technology")
st.text("Artificial Intelligence and Data Science")
st.write("Choose your favourite Elective")

subject = st.selectbox("Select Subject", ["Research", "Time Series", "Machine Learning"])
st.write(f"You choose {subject} subject. Congratulations")

st.success("Subject has been successfully verified")