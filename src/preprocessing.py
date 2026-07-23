import numpy as np
import pandas as pd

#Analisis de cohortes (cada mes se trata de forma individualizada para comparar patrones mes a mes)
def build_cohort_table(df):
    months = sorted(
        [col for col in df.columns if col.startswith("M")],
        key=lambda x: int(x[1:])
    )

    result = pd.DataFrame( #Tabla vacia con NaN para almacenar los resultados
        np.nan,
        index=months,
        columns=months
    )

    for i, current_month in enumerate(months): #Bucle para calcular la retención de cada cohorte
        previous_months = months[:i]

        cohort_mask = df[current_month].eq(1) #Máscara para seleccionar clientes del cohorte actual

        if previous_months: #Si hay meses anteriores, asegurarse de que los clientes no hayan comprado en esos meses
            cohort_mask &= df[previous_months].eq(0).all(axis=1)

        cohort = df[cohort_mask] #Seleccionar los clientes del cohorte actual con mascara final

        if cohort.empty: #si la cohorte esta vacia, nobe hagas nada y vuelve a la siguiente iteración
            continue

        result.loc[current_month, current_month:] = ( #Calcular la retención de los clientes del cohorte actual en los meses siguientes
            cohort.loc[:, current_month:].mean() * 100
        )

    return result