import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração básica da página
st.set_page_config(
    page_title="🔍 Análise de Qualidade",
    page_icon="🔍",
    layout="wide"
)

# Carregar dados simplificados
def load_data():
    data = {
        "Categoria": ["Eletrônicos", "Roupas", "Alimentos", "Móveis", "Brinquedos"],
        "Taxa_Defeitos": [2.5, 3.1, 1.8, 4.2, 2.0]
    }
    return pd.DataFrame(data)

df = load_data()

# Título principal
st.title("🔍 Análise de Qualidade")
st.write("Uma visão simplificada dos defeitos por categoria.")

# KPI simplificado
st.metric(label="❌ Taxa Média de Defeitos", value=f"{df['Taxa_Defeitos'].mean():.2f}%")

# Gráfico único: Distribuição de Defeitos por Categoria
st.subheader("📌 Distribuição de Defeitos por Categoria")
fig = px.bar(df, x="Categoria", y="Taxa_Defeitos", color="Categoria", text_auto=True)
st.plotly_chart(fig, use_container_width=True)

# Rodapé
st.write("📌 Esta é uma versão simplificada do dashboard. A versão completa inclui mais análises e interatividade.")
