import streamlit as st

st.title(":green[Asistente virtual del curso de Tecnología de la leche]")

st.image("https://luisartica.wordpress.com/wp-content/uploads/2020/04/tecnologia-de-leche-ii.jpg?w=259")

import streamlit as st
st.title("Bienvenido, aprenderás mucho del mundo de la leche y sus productos")

# Widget: text_input
nombre = st.text_input("Escribe tu nombre")

if nombre:
    st.write(f"Hola, {nombre} 👋")
