import streamlit as st

st.title('Streamlit Example')
st.write('Hello World! :sunglasses:')
x = st.text_input('Favorte Movie')
st.write(f'Your favorite movie is: {x}')

is_clicked = st.button('Click Me')
