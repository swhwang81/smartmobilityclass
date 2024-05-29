import streamlit as st 


def bmi_range(bmi):
    if bmi>=25:
        st.erro("비만입니다.")
    elif bmi >=23:
        st.warning("과체중입니다.")
    elif bmi >=18.5:
        st.success("정상입니다.")
    else:
        st.warning("저체중입니다.")
    


st.title("체질량지수 계산기")

st.info("체질량지수는 자신의 몸무게를 키의 제곱으로 나눈 값입니다.")

height = st.number_input("신장 (cm)", value= 160, step =1)
st.write(f"당신의 신장은 : {height} cm")

width = st.number_input("체중 (kg)", value= 60, step =1)
st.write(f"당신의 체중은 : {width} kg")

bmi = width/((height/100)**2)

if st.button("계산하기!"):
    st.write(f"당신의 체질량지수는 {round(bmi,2)} 입니다.")
    bmi_range(bmi)
    st.balloons()
    
    
        
st.image("vegi.jpg",caption="균형있는 식단과 적절한 운동이 필수입니다!")