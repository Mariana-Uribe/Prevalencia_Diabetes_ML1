# Proyecto integrador — entrega final ML I
Jean Paul Rojas Rojas y Mariana Uribe Vanegas

## Ejecución

1. Python 3.10+; abrir terminal dentro de esta carpeta.
2. `pip install -r requirements.txt`
3. `python modelado.py` — genera modelo y tablas/gráficos reproducibles.
4. `streamlit run app.py` — abre la interfaz en el navegador.

## Estructura
- `datos/`: CSV entregado por el equipo (8.475 observaciones).
- `modelado.py`: separación por hogar, validación cruzada agrupada, búsqueda ampliada, umbral fuera de pliegue, evaluación, bootstrap, odds ratios, errores por subgrupo y artefacto predictivo.
- `modelos/modelo_diabetes.joblib`: pipeline **completo** más umbral y categorías.
- `resultados/`: evidencia del informe (CSV, JSON y PNG).
- `app.py`: interfaz Streamlit que usa el pipeline sin ajustar transformaciones nuevas.

## Advertencias metodológicas

- **Origen**: el archivo se identifica como ENSANUT 2025, pero el CSV no prueba la procedencia, el diseño muestral, la metodología de recolección ni las variables originales. Identificar y enlazar la institución, país, catálogo y documentación oficiales antes de declarar representatividad mexicana. Tampoco podemos certificar que estas 8.475 filas sean microdatos originales sin el respaldo de la fuente.
- **Prueba ya consultada**: en la fase 2 se evaluó el 20% por individuos. En esta entrega se rehace una partición por hogares, pero el mismo dataset ya influyó en decisiones previas; NO debe anunciarse como validación externa completamente ciega.
- El conjunto de prueba **no** determina hiperparámetros, elección final ni umbral en este script.
- Se usa `StratifiedGroupKFold` para evitar hogares compartidos, admitiendo pequeñas variaciones en tamaños de pliegue y prevalencia.
- Las odds ratios de L2 penalizada, con peso balanceado, son asociaciones ajustadas descriptivas, no efectos causales ni estimadores inferenciales clásicos; numéricas por desviación estándar.
- La puntuación de Streamlit **no** está calibrada ni validada para decisiones de salud. Tampoco se verificó estabilidad temporal o externa.
- La validación interna puede ser optimista si la decisión final entre familias de modelos se guía por los mismos pliegues; se privilegió logística por interpretación y sensibilidad y no se seleccionó usando la prueba de esta ejecución.

## Declaración académica
Se utilizó IA generativa como herramienta de apoyo para estructurar, redactar y depurar código. Los integrantes deben revisar, ejecutar y poder justificar todo el trabajo. Las bibliotecas usadas son pandas, numpy, scikit-learn, matplotlib, joblib y Streamlit.
