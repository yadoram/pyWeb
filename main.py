import streamlit as st
import pandas as pd

st.title('2022년도 지하철 월별 하차 인원')

df = pd.read_csv('monthly_subway_statistics_in_seoul.csv')
df.set_index = df['연번']

if st.button('data copyright link'):
    st.write('https://www.data.go.kr/data/15044247/fileData.do')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.subheader('역별 하차 인원')
option = st.selectbox(
    '역 선택', 
    (df['역명']))

mask= df['역명'].isin([option])
df_grouped = df[mask].groupby(by=['수송연월']).sum()[['하차인원수']]
df_grouped = df_grouped.reset_index()
st.bar_chart(df_grouped, x='수송연월')


st.subheader('호선별 하차 인원')
df_line = df.groupby('호선').sum()
lines = df_line.index.tolist()
option = st.selectbox(
    '호선 선택', 
    (lines))

mask= df['호선'].isin([option])
df_grouped = df[mask].groupby(by=['수송연월']).sum()[['하차인원수']]
df_grouped = df_grouped.reset_index()
st.area_chart(df_grouped, x='수송연월')


