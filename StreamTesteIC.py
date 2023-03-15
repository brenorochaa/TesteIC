import streamlit as st
from PIL import Image
img = open('random_logo.png')
st.image(img, caption = 'Random UFPE')
st.title("Engenharia de Manutenção - RANDOM UFPE")
st.header("Políticas de manutenção por idade")
st.subheader("Como encontrar os parâmetros Beta e Eta pra a distribuição Weibull")
st.write("Encontrar os parâmetros Beta e Eta para se aplicar na distribuição de probabilidade Weibull não é uma tarefa fácil. Para isso, desenvolvemos esta ferramenta de modo que utiliza dados estatísticos a fim de simplificar o processo de obtenção desse resultado")
if st.checkbox("Estou disposto a participar"):
    st.text("Muito bem! vamos nessa!")
nome = st.text_input("Qual o seu nome?")
st.write("nome registrado!")
status = st.selectbox("Qual sua atuação: ", ['Estudante', 'Professor', 'Outro'])
st.write('Sua opção escolhida foi: ',status)
