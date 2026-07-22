import streamlit as st

GLOSARIO = [
    ("IEC (Índice de Efectividad de Conectividad)",
     "Un puntaje de 0 a 100 que resume qué tan bien le va a un municipio en lo educativo. "
     "Se calcula combinando retención estudiantil, cobertura escolar y tasa de aprobación."),
    ("Efectividad (Alto / Medio / Bajo)",
     "Compara al municipio contra otros parecidos que NO tienen Centro Digital. Si un municipio "
     "supera bastante a esos similares, su efectividad es 'Alta' — aunque su IEC en términos "
     "absolutos no sea muy alto."),
    ("Retención estudiantil",
     "Qué tantos estudiantes se quedan en el colegio en vez de abandonarlo (lo contrario a la "
     "deserción escolar). Más alto es mejor."),
    ("Cobertura escolar",
     "Qué porcentaje de niños y jóvenes en edad escolar (5 a 16 años) están efectivamente "
     "matriculados en el grado que les corresponde."),
    ("Tasa de aprobación",
     "Qué porcentaje de estudiantes matriculados aprueba el año escolar."),
]


def render_glosario():
    st.markdown("#### 📖 Glosario de términos")
    for termino, definicion in GLOSARIO:
        with st.expander(termino):
            st.markdown(definicion)
