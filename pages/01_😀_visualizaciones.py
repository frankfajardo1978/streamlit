
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import subprocess
import sys




if st.checkbox("mostrar texto"):
    st.write('Hola Alexa Camila')

data = pd.read_csv('Vehicle_Fuel_Economy_Optimized (1).csv')

if st.checkbox('mostra data'):
    st.dataframe(data)

if st.checkbox('vista de head o tail'):
    if st.button('mostrar head'):
        st.write(data.head())
    if st.button('Mostrar tail'):
        st.write(data.tail())

dim = st.radio('Dimension a mostrar',('filas','columnas'),horizontal = True)

if dim == 'filas':
    st.write('la cantidad de filas',data.shape[0])
else:
    st.write('la cantidad de columnas',data.shape[1])


data2arr = np.random.randn(100,5)
data2 = pd.DataFrame(data2arr)

if st.checkbox('mostrar data2'):
    st.dataframe(data2)

st.slider('definir valor maximo',0,4000,250)

fig = plt.figure(figsize = (6,4))
sns.scatterplot(x = data2[0], y = data2[1],data = data2)
st.pyplot(fig)

