"""Aplicación académica de tamizaje, NO herramienta de diagnóstico."""
from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

BASE=Path(__file__).resolve().parent
st.set_page_config(page_title='Proyecto ML I — Diabetes',layout='centered')
st.title('Clasificación exploratoria de diabetes')
st.warning('Uso exclusivamente académico. No diagnostica diabetes ni sustituye una evaluación clínica. Las probabilidades no están calibradas clínicamente.')
archivo=BASE/'modelos'/'modelo_diabetes.joblib'
if not archivo.exists():
    st.error('Falta el modelo. Ejecuta primero todas las celdas del notebook.')
    st.stop()
a=joblib.load(archivo)
st.caption(f"Modelo: regresión logística L2, umbral de clasificación {a['umbral']:.3f}, validado separando hogares.")
nums={'EDAD':(20,100,45),'IMC':(12.,70.,28.),'PAS_MEDIA':(70.,250.,125.),'PAD_MEDIA':(40.,150.,80.)}
with st.form('prediccion'):
    valores={}
    st.subheader('Datos de la persona adulta')
    for c,(mn,mx,default) in nums.items():
        valores[c]=st.number_input(c,min_value=mn,max_value=mx,value=default)
    for c, opciones in a['categorias'].items():
        valores[c]=st.selectbox(c,opciones)
    for c in ['HIPERTENSION','COLESTEROL_ALTO','TRIGLICERIDOS_ALTOS','ENF_RENAL','ENF_CARDIOVASCULAR','DIF_CAMINAR','SIN_SEGURO_SALUD','TRABAJA']:
        valores[c]=int(st.checkbox(c,value=False))
    enviar=st.form_submit_button('Estimar clasificación')
if enviar:
    fila=pd.DataFrame([valores],columns=a['features'])
    prob=float(a['pipeline'].predict_proba(fila)[0,1])
    detectado=prob>=a['umbral']
    st.metric('Puntuación del modelo',f'{prob:.1%}')
    st.write('**Clasificación de tamizaje:**','Positiva' if detectado else 'Negativa')
    st.info('Esta puntuación refleja el comportamiento del modelo en el conjunto de estudio y no es una probabilidad clínica individual validada. Consulte a un profesional de salud para pruebas de diagnóstico.')
