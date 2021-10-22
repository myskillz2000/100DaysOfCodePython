import streamlit as st
import pandas as pd


# Navagation bar type progress
# Create multiple views with if statements in sidebar.
st.title("Bridges to Success")

button1 = st.button("Click Me!")
if button1:
    st.write("The Button Works")
else:
    pass
st.header("Have you been incarcerated?")
incarcerated = st.checkbox("Yes")
not_incarcerate = st.checkbox("No")
button2 = st.button("Submit")
if button2:
    if incarcerated:
        st.write("Thanks for your input!")
    else:
        st.write("Thanks for your input 1.")

st.header("Radio examples")

training = st.radio("What training do you want?", ('OSHA', 'Microsoft', 'Forklift'))
button3 = st.button("Submit training")
if button3:
    st.write(training)
    if training == "OSHA":
        st.write("You have selected OSHA")
    elif training == "Microsoft":
        st.write("You have selected Microsoft")
    else:
        st.write("You have selected Forklift")

# st.selectbox("What are you looking for?", ("Lion", "Tiger", "Bear"))
st.header("Start of the multiselct Section")
options = st.multiselect("What do you like?",
          ["Lion", "Tiger", "Bear"])

button5 = st.button("Print Animals")
if button5:
    st.write(options)
# st.slider("How many epochs?", 1,100, 10)
# st.text_input()
# st.number_input()
# st.text_area()

#Layout section.  Sidebar and columns and expander
# st.sidebar.image How to add images can control height and width.
st.sidebar.header("Option possibilities")
text = st.sidebar.text_area("Paste Text Here")
buttonsidebar = st.sidebar.button("Clean Text")
if buttonsidebar:
    st.write(text)

# st.beta_columns(2)
# st.beta_expander()  use an with statement.

# Forms
# st.form

# Containers
# st.beta_container()