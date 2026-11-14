# Prevalencia y predictores de diabetes · Machine Learning I

**Jean Paul Rojas Rojas y Mariana Uribe Vanegas** · Universidad Externado de Colombia · 2026.

## Contenido

- `Entrega_Final_ML1_COMPLETO.ipynb`: análisis, entrenamiento, validación por hogar, métricas, interpretaciones, gráficas y conclusiones. **Las salidas se muestran dentro del cuaderno; no se exportan CSV, Excel, JSON ni PNG.**
- `datos/base_diabetes_ensanut2025.csv`: datos suministrados al equipo. Verificar país, institución, origen y permisos antes de difusión pública.
- `modelos/modelo_diabetes.joblib`: modelo exportado para Streamlit; ejecutar el notebook para regenerarlo.
- `app.py`: aplicación Streamlit independiente de otros scripts .py.
- `requirements.txt`: dependencias.

## Cómo usarlo

1. Abre **esta carpeta** en VS Code o Jupyter.
2. Selecciona un kernel Python 3.11/3.12 con las dependencias instaladas.
3. En una terminal, ejecuta `python -m pip install -r requirements.txt`.
4. Abre `Entrega_Final_ML1_COMPLETO.ipynb` y ejecuta **Run All**.
5. Para el despliegue local, ejecuta `streamlit run app.py` en la misma carpeta.

**Cuidado:** la aplicación no diagnostica diabetes. La base y las cifras no son una validación clínica independiente. El equipo debe declarar el uso de herramientas de IA como apoyo y poder sustentar cada decisión. No publicar datos sensibles sin autorización.
