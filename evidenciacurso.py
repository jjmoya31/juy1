import streamlit as st

st.title(":red[Asistente virtual del curso de Tecnología de la leche]")

st.image("https://luisartica.wordpress.com/wp-content/uploads/2020/04/tecnologia-de-leche-ii.jpg?w=259")

# 02_entrada_texto.py
import streamlit as st

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.write(f"Hola, {nombre} 👋")
