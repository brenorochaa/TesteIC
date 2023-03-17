import numpy as np
import stats
import streamlit as st


def ajuste_weibull():
    
    data_str = str(dados)
    data = np.fromstring(data_str,sep =',') 
    
    parameters_1 = stats.exponweib.fit(data,floc=0,f0=1)
    fitness_1 = stats.kstest(data,"exponweib",parameters_1)
    
    p_forma = parameters_1[1]
    p_escala = parameters_1[3]
    
    p_valor = fitness_1[1]
    
    if p_valor < 0.05:
        
        st.write(f'''
        Parâmetro de forma = {p_forma}
        Parâmetro de escala = {p_escala}
        
        Teste de hipótese:
        p-valor = {p_valor}
        
        Com um nível de significância de 5%,
        REJEITA-SE a hipótese de que os dados 
        seguem uma distribuição Weibull''')
        
    else:
        st.write(f'''
        Parâmetro de forma = {p_forma}
        Parâmetro de escala = {p_escala}
        
        Teste de hipótese:
        p-valor = {p_valor}
        
        Com um nível de significância de 5%,
        ACEITA-SE a hipótese de que os dados 
        seguem uma distribuição Weibull''')
        

def ajuste_exponencial():
    
    data_str = str(dados)
    data = np.fromstring(data_str,sep =',') 
    
    parameters_2 = stats.expon.fit(data,floc=0)
    fitness_2 = stats.kstest(data,"expon",parameters_2)
    
    escala = parameters_2[1]
    tx = 1/escala
    
    p_valor = fitness_2[1]
    
    if p_valor < 0.05:
        
        st.write(f'''
        Taxa (lambda) = {tx}
        
        Teste de hipótese:
        p-valor = {p_valor}
        
        Com um nível de significância de 5%,
        REJEITA-SE a hipótese de que os dados 
        seguem uma distribuição exponencial''')
        
    else:
        st.write(f'''
        Taxa (lambda) = {tx}
        
        Teste de hipótese:
        p-valor = {p_valor}
        
        Com um nível de significância de 5%,
        ACEITA-SE a hipótese de que os dados 
        seguem uma distribuição exponencial''')
        

st.title('Ajuste de distribuições de probabilidade')

st.markdown('Insira os dados separados por vírgula')
dados = st.text_input(label='Dados')

if st.button('Distribuição Weibull'):
    ajuste_weibull()

if st.button('Distribuição Exponencial'):
    ajuste_exponencial()
