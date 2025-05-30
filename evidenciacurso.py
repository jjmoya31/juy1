import streamlit as st

st.sidebar.title(":green[Asistente virtual del curso de Tecnología de la leche]")
st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwjLZoqdSVYx60Zw7ieTIvL-GSqM29w2GcoSz0e3nVvVtbBq6OvMQ1Bs1l2dBnn4axXNc&usqp=CAU")

st.image("https://luisartica.wordpress.com/wp-content/uploads/2020/04/tecnologia-de-leche-ii.jpg?w=500")

import streamlit as st
st.write("Bienvenido a el curso de Tecnología de la leche, aprenderás mucho del mundo de la leche y sus productos")

# Widget: text_input
nombre = st.text_input("Escribe tu nombre")

if nombre:
    st.write(f"Hola, {nombre} 👋")

multi = '''Contenido: 
* 1.Situación Láctea  
* 2.Composición de la leche  
* 3.Propiedades y calidad  
* 4.Microbiología de la leche
'''
st.write(multi)

st.write("Instrucciones: anota en el buscador un tema del contenido para iniciar el aprendizaje")

import streamlit as st
from openai import OpenAI


# Show title and description.
st.title("💬 Chatbot")
st.write(
    "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
    "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("What is up?"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

