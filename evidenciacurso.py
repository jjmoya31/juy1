st.image("https://lh4.googleusercontent.com/proxy/G5-2LYxrjTbpNJCjU_PWqa6MPNu8tOZVtc_6bhfw-g5QH_LqGYsqLE5GBzY9Yq3MHil-UkEN3jJrt3oPP8vbQbUGbN2goMwZQntMm0xe4B6ZdqH2Cbb6Rri5GgQ31Y73Wue_DKkEIaboIN4")

import streamlit as st

st.title(":green[Asistente virtual del curso de Tecnología de la leche]")

st.image("https://luisartica.wordpress.com/wp-content/uploads/2020/04/tecnologia-de-leche-ii.jpg?w=500")

import streamlit as st
st.write("Bienvenido a el curso de Tecnología de la leche, aprenderás mucho del mundo de la leche y sus productos")

# Widget: text_input
nombre = st.text_input("Escribe tu nombre")

if nombre:
    st.write(f"Hola, {nombre} 👋")



import streamlit as st
st.write("Contenido 1.Situación Láctea 2.Composición de la leche 3.Propiedades y calidad 4.Microbiología de la leche")
