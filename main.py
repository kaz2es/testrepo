import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門')

st.write('DataFrame')

st.write('Display Image')




img=Image.open('証明写真.jpg')
st.image(img, caption='Shimauchi Kazuhiro',use_columns_width=True)

# st.table(df.style.highlight_max(axis=0))
#st.area_chart(df)