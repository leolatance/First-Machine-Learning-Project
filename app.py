import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("manutencao.csv")

modelo = LinearRegression()
x = df[["temperatura_forno"]]
y = df[["resistencia_aco"]]

modelo.fit(x, y)

st.title("Prevendo a resistencia do aço em relaçao a temperatura do forno")
st.divider()

diametro = st.number_input("Digite a temperatura do forno: ")
if diametro:
    temperatura_prevista = modelo.predict([[diametro]])[0][0]
    st.write(f"A resistencia prevista para a temperatura de {diametro:.2f} ° é de {temperatura_prevista:.2f} MPa")   