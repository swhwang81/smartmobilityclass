import streamlit as st

def bmi_range(bmi):
    if bmi>= 25:
        st.error("비만 입니다!")
    elif bmi >=23:
        st.warning('과체중 입니다!')
    elif bmi >= 18.5:
        st.success('정상 입니다!')
    else:
        st.warning('저체중 입니다!')