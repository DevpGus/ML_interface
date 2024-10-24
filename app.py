import streamlit as st
import pickle
import numpy as np

def load_model():
    model = pickle.load(open('trained_model.sav', 'rb'))
    return model

model = load_model()

st.title("Previsão de Diabetes")
st.write('Este é um aplicativo criado para previsão de portadores de diabetes, com base em um modelo de machine learning.')
st.subheader('Preencha as seguintes informações:')

grav = st.number_input('Quantidade de vezes em gestação: ', min_value=0, max_value=20, step=1)
gli = st.number_input('Concentração de glicose: ', min_value=0, max_value=400, step=1)
pres = st.number_input('Pressão sanguínea: ', min_value=0, max_value=300, step=1) 
esp = st.number_input('Espessura da pele: ', min_value=0, max_value=1000, step=1)
ins = st.number_input('Insulina: ', min_value=0, max_value=1000, step=1)
imc = st.number_input('IMC: ', min_value=0.0, max_value=50.0, step=0.1)
ped = st.number_input('Função de pedigree de diabetes: ', min_value=0.000, max_value=4.000, step=0.001)
id = st.number_input('Idade (anos):', min_value=0, max_value=99, step=1)

b_prever = st.button('Prever')

def main():
    if b_prever: 
        arr2d = np.array([[grav, gli, pres, esp, ins, imc, ped, id]])
        prediction = model.predict(arr2d)
        
        if prediction == [1]:
            st.write('A pessoa é portadora de diabetes.')
        elif prediction == [0]:
            st.write('A pessoa não é portadora de diabetes.')
        else:
            st.write('Não foi possível realizar previsão.')
        return
    
main()