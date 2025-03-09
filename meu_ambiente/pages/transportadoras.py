import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração básica da página
st.set_page_config(
    page_title="🚚 Análise de Transportadoras",
    page_icon="🚚",
    layout="wide"
)

# Carregar dados simplificados
def load_data():
    data = {
        "Modalidade": ["Aéreo", "Rodoviário", "Ferroviário", "Marítimo"],
        "Custo_Médio": [1200, 800, 650, 500]
    }
    return pd.DataFrame(data)

df = load_data()

# Título principal
st.title("🚚 Análise de Transportadoras")
st.write("Uma visão simplificada dos custos médios por modalidade de transporte.")

# KPI simplificado
st.metric(label="💰 Custo Médio de Envio", value=f"R$ {df['Custo_Médio'].mean():,.2f}")

# Gráfico único: Custos Médios por Modalidade
st.subheader("📌 Custos Médios por Modalidade de Transporte")
fig = px.bar(df, x="Modalidade", y="Custo_Médio", color="Modalidade", text_auto=True)
st.plotly_chart(fig, use_container_width=True)

# Rodapé
st.write("📌 Esta é uma versão simplificada do dashboard. A versão completa inclui mais análises e interatividade.")
