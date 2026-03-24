import streamlit as st
import pandas as pd
import plotly.express as px
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Hype Track", page_icon="📈", layout="wide")

@st.cache_data
def carregar_dados():
    produtos = ['Óculos VR Neo', 'Smartphone Holográfico', 'Neural Link Lite', 'Console Quântico']
    sentimentos = ['Positivo', 'Neutro', 'Negativo']
    
    dados = []
    hoje = datetime.now()
    
    for _ in range(200):
        dados.append({
            "Data": hoje - timedelta(days=random.randint(0, 30)),
            "Produto": random.choice(produtos),
            "Sentimento": random.choice(sentimentos),
            "Engajamento": random.randint(100, 5000),
            "Nota": random.uniform(1, 5)
        })
    
    return pd.DataFrame(dados)

df = carregar_dados()

st.sidebar.header("🛠️ Painel de Controle")
st.sidebar.markdown("Filtre os dados em tempo real:")
produto_selecionado = st.sidebar.multiselect(
    "Escolha o Produto:",
    options=df["Produto"].unique(),
    default=df["Produto"].unique()
)

df_filtrado = df[df["Produto"].isin(produto_selecionado)]

st.title("📈 Rastreador de Hype")
st.subheader("Análise visual de sentimentos e engajamento tech")
st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Menções", len(df_filtrado), "+12%")
with col2:
    st.metric("Média de Engajamento", f"{int(df_filtrado['Engajamento'].mean())} cliques")
with col3:
    st.metric("Nota Média", round(df_filtrado['Nota'].mean(), 1), "⭐")
    
st.markdown("---")

col_esq, col_dir = st.columns(2)

with col_esq:
    st.markdown("### 🔥 Volume de Hype por Produto")
    fig_bar = px.bar(df_filtrado, x="Produto", y="Engajamento", color="Sentimento",
                     title="Engajamento Total por Categoria",
                     color_discrete_map={'Positivo':'#00CC96', 'Neutro':'#636EFA', 'Negativo':'#EF553B'})
    st.plotly_chart(fig_bar, use_container_width=True)
    
with col_dir:
    st.markdown("### 🧠 Distribuição de Sentimento")
    fig_pie = px.pie(df_filtrado, names="Sentimento", hole=0.4,
                     title="O que o mundo está achando?")
    st.plotly_chart(fig_pie, use_container_width=True)
    
with st.expander("📂 Ver dados brutos (Tabela do Pandas)"):
    st.dataframe(df_filtrado.sort_values(by="Data", ascending=False),
                 use_container_width=True)
    
st.sidebar.info("Projeto criado para o tutorial de Python do Descomplica Dev!")
    