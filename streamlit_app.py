import streamlit as st
import pandas as pd

st.title('Streamlit Example')
st.write('Hello World! :sunglasses:')
x = st.text_input('Favorte Movie')
st.write(f'Your favorite movie is: {x}')
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))

is_clicked = st.button('Click Me')
