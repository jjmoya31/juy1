# carga la libreria streamlit como "st"
import streamlit as st
# asignar un titulo
st.title("Mi primer app en Streamlit")
# agregar un boton
st.button("click")
# agregar globos
st.balloons()

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)


import datetime
import streamlit as st

d = st.date_input("When's your birthday", value=None)
st.write("Your birthday is:", d)

st.image("https://static.nationalgeographicla.com/files/styles/image_3200/public/1160.jpg?w=1900&h=1426")
