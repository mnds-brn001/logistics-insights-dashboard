import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração básica da página
st.set_page_config(
    page_title="📊 Supply Chain Dashboard",
    page_icon="📦",
    layout="wide"
)

# Carregar dados simplificados
def load_data():
    data = {
        "Categoria": ["Eletrônicos", "Roupas", "Alimentos", "Móveis", "Brinquedos"],
        "Quantidade_Vendida": [1500, 2300, 1200, 800, 950],
        "Receita_Gerada": [75000, 92000, 34000, 56000, 29000]
    }
    return pd.DataFrame(data)

df = load_data()

# Título principal
st.title("📊 Supply Chain Dashboard")
st.write("Uma visão geral simples das vendas por categoria.")

# KPIs simplificados
col1, col2 = st.columns(2)

with col1:
    st.metric(label="💰 Receita Total", value=f"R$ {df['Receita_Gerada'].sum():,.2f}")

with col2:
    st.metric(label="📦 Total de Vendas", value=f"{df['Quantidade_Vendida'].sum():,}")

# Gráfico único: Distribuição de Vendas por Categoria
st.subheader("📌 Distribuição de Vendas por Categoria")
fig = px.bar(df, x="Categoria", y="Quantidade_Vendida", color="Categoria", text_auto=True)
st.plotly_chart(fig, use_container_width=True)

# Rodapé
st.write("📌 Esta é uma versão simplificada do dashboard. A versão completa inclui mais análises e interatividade.")
