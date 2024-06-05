import streamlit as st 
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def bmi_range(bmi):
    if bmi>= 25:
        st.error("비만 입니다!")
    elif bmi >=23:
        st.warning('과체중 입니다!')
    elif bmi >= 18.5:
        st.success('정상 입니다!')
    else:
        st.warning('저체중 입니다!')


selected = st.sidebar.selectbox(
    "목차",
    ("체질량 계산기", "갭마인더", "국가별")
)

if selected =='체질량 계산기':

    st.header('체질량 지수 계산기')

    st.info('체질량지수는 자신의 몸무게를 키의 제곱으로 나눈 값입니다.')

    height = st.number_input('신장 (cm)',value = 160, step =5)
    st.write(height,'cm')

    weight = st.number_input('체중 (kg)', value = 50, step =5)
    st.write(weight,'kg')

    bmi = weight/((height/100)**2)

    if st.button('계산'):
        st.write('당신의 체질량 지수는', round(bmi,2), '입니다.')
        bmi_range(bmi)
        
        
    image = Image.open('vegetables.jpg')

    st.image(image, caption='eat a lot of vegetables!')
        
elif selected == '갭마인더':
    st.header('Gapminder 분석')

    st.write('파일 읽어오기 ')

    data = pd.read_csv('gapminder.csv')

    #st.write(data)

    colors = []
    for x in data['continent']:
        if x == 'Asia':
            colors.append('tomato')
        elif x =='Europe':
            colors.append('blue')
        elif x == 'Africa':
            colors.append('olive')
        elif x =='Americas':
            colors.append('green')
        else:
            colors.append('orange')

    data['colors'] = colors 

    year = st.slider('Select a Year', 1952, 2007, 1952, step = 5)
    st.write('## ', year, '년')

    data = data[data['year']==year]

    fig, ax = plt.subplots()
    ax.scatter(data['gdpPercap'],data['lifeExp'],s=data['pop']*0.000002, color = data['colors'])
    ax.set_title('How Does Gdp per Capital relate to Life Expectancy?')
    ax.set_xlabel("Gdp per Capital")
    ax.set_ylabel('Life Expectancy')
    st.pyplot(fig)

    #st.write('(Asia: tomato, Europe: blue, Africa: olive, Americas: green, others: orange)')
    
else:
    st.header('My Gapminder')
    dic ={}
    data = pd.read_csv('gapminder.csv')

    #st.write(data['continent'].value_counts())

    #st.write(data)
    #countries = data['country'].value_counts().index
    #st.write(countries)
    #st.write(data['country'].unique())
    countries = data['country'].unique()
    options = st.multiselect(
        'Choose Countries',
        countries,
        ['Korea, Rep.'])

    #st.write(options)

    fig, ax = plt.subplots()
    for x in options:
        ax.plot(range(len(data[data['country']==x]['pop'])),data[data['country']==x]['pop'],label=x)
    ax.legend()
    ax.set_title('Poplation Growth')
    ax.set_xticks(range(len(data[data['country']==x]['pop'])),data[data['country']==x]['year'])
    st.pyplot(fig)
        
        

    fig1, ax1 = plt.subplots()
    for x in options:
        ax1.plot(range(len(data[data['country']==x]['lifeExp'])),data[data['country']==x]['lifeExp'],label=x)
    ax1.legend()
    ax1.set_xticks(range(len(data[data['country']==x]['pop'])),data[data['country']==x]['year'])
    ax1.set_title('Life Expectancy')
    st.pyplot(fig1)
    

    data2007 = data[data['year']==2007]
    
    data2007.reset_index(drop=True, inplace=True)
    #st.write(data2007)
    colors =[]
    for i in range(len(data2007)):
        colors.append("skyblue")
    
    
    for x in options: 
        loc = data2007[data2007['country'] == x].index[0]
        colors[loc] = "red"
    
    fig0, ax0 = plt.subplots()
    ax0.scatter(data2007['lifeExp'],data2007['gdpPercap'],s = data2007['pop']*0.000001, color=colors)
    
    for x in options: 
        loc = data2007[data2007['country'] == x].index[0]
        ax0.annotate(x,(data2007["lifeExp"][loc],data2007['gdpPercap'][loc]))
    
    st.pyplot(fig0)
    
    #st.write(data2007['gdpPercap'][loc])
