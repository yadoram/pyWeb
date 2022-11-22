import streamlit as st
import numpy as np
import pandas as pd

st.write('# web test :sunglasses:')

st.write('## Chart:heart:')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)