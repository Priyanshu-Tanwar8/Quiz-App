import streamlit as st
import questionBank as qz

st.title('Python Programming Quiz🐍')
st.header("Welcome To The Python Quiz")

count = 0


st.title("")
question = st.radio(
    qz.question[0],
    qz.responses[0],)

if question == qz.answer[0]:
    count += 1

question = st.radio(
    qz.question[1],
    qz.responses[1],)

if question == qz.answer[1]:
    count += 1

question = st.radio(
    qz.question[2],
    qz.responses[2],)

if question == qz.answer[2]:
    count += 1

question = st.radio(
    qz.question[3],
    qz.responses[3],)

if question == qz.answer[3]:
    count += 1

question = st.radio(
    qz.question[4],
    qz.responses[4],)

if question == qz.answer[4]:
    count += 1

question = st.radio(
    qz.question[5],
    qz.responses[5],)

if question == qz.answer[5]:
    count += 1

question = st.radio(
    qz.question[6],
    qz.responses[6],)

if question == qz.answer[6]:
    count += 1

question = st.radio(
    qz.question[7],
    qz.responses[7],)

if question == qz.answer[7]:
    count += 1

question = st.radio(
    qz.question[8],
    qz.responses[8],)

if question == qz.answer[8]:
    count += 1

question = st.radio(
    qz.question[9],
    qz.responses[9],)

if question == qz.answer[9]:
    count += 1

if st.button('Submit'):
    st.title('You got ' + str(count) + ' correct')
    if count == 10:
        st.balloons()
    elif count < 5:
        st.snow()

