import streamlit as st
import pandas as pd
import numpy as np 

st.title('2022년도 지하철 월별 하차 인원 🛤️')

df = pd.read_csv('monthly_subway_statistics_in_seoul.csv')
df.set_index = df['연번']

if st.button('data copyright link'):
    st.write('https://www.data.go.kr/data/15044247/fileData.do')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.subheader('🚅 역별 하차 인원')
option = st.selectbox(
    '역 선택', 
    (df['역명']))

mask= df['역명'].isin([option])
df_grouped = df[mask].groupby(by=['수송연월']).sum()[['하차인원수']]
df_grouped = df_grouped.reset_index()
st.bar_chart(df_grouped, x='수송연월')


st.subheader('🚅 호선별 하차 인원')
df_line = df.groupby('호선').sum()
lines = df_line.index.tolist()
option = st.selectbox(
    '호선 선택', 
    (lines))

mask= df['호선'].isin([option])
df_grouped = df[mask].groupby(by=['수송연월']).sum()[['하차인원수']]
df_grouped = df_grouped.reset_index()
st.area_chart(df_grouped, x='수송연월')


# pd.read_csv를 통하여 승하차 인원 정보 데이터를 데이터프레임 형태로 읽어옵니다.
metro_all = pd.read_csv("서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.csv", encoding = 'cp949')


# metro_all DataFrame 사용월 데이터 확인
sorted(list(set(metro_all['사용월'])))
# metro_all DataFrame 호선명 데이터 확인
sorted(list(set(metro_all['호선명'])))
# DataFrame 지하철역 데이터 확인
sorted(list(set(metro_all['지하철역'])))
# DataFrame 지하철역 데이터 개수 확인
len(list(set(metro_all['지하철역'])))

st.subheader('🚅 선택한 월의 총 승객수 🚶‍♂️')
metro_all_line = metro_all.groupby('사용월').sum()
lines = metro_all_line.index.tolist()
option = st.selectbox(
    '사용월 선택', 
    (lines))

# 선택한 월의 총 승객수만 추출
metro_recent = metro_all[metro_all['사용월']==option]

# 불필요한 작업일자 컬럼 제거
metro_recent = metro_recent.drop(columns={'작업일자'})

metro_line = metro_recent.groupby(['호선명']).mean().reset_index()
metro_line = metro_line.drop(columns='사용월').set_index('호선명')
metro_line = metro_line.mean(axis=1).sort_values(ascending=False)

st.bar_chart(metro_line)
