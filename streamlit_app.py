import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Streamlit Example')
st.write('Hello World! :sunglasses:')
x = st.text_input('Favorte Movie')
st.write(f'Your favorite movie is: {x}')
st.subheader('This is a subheader with a divider', divider='rainbow')
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

is_clicked = st.button('Click Me')
