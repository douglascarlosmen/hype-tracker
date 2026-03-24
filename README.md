# 📈 Hype Track

Dashboard interativo em **Streamlit** para acompanhar hype de produtos de tecnologia com foco em:
- volume de menções
- engajamento por produto
- distribuição de sentimento
- visualização de dados brutos

O projeto usa dados simulados para demonstrar análise visual rápida com **Pandas** e **Plotly**.

## ✨ Funcionalidades

- Interface web com layout amplo e responsivo
- Filtro por produto na barra lateral
- Métricas de resumo em tempo real:
  - total de menções
  - média de engajamento
  - nota média
- Gráfico de barras por produto e sentimento
- Gráfico de pizza para distribuição de sentimento
- Tabela com dados filtrados e ordenados por data
- Cache de dados com `st.cache_data` para melhor performance

## 🧱 Stack

- Python 3.10+ (recomendado)
- Streamlit
- Pandas
- Plotly Express

## 📂 Estrutura do projeto

```text
video/
├─ app.py
└─ README.md
```

## 🚀 Como executar

### 1) Criar e ativar ambiente virtual (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2) Instalar dependências

```powershell
pip install streamlit pandas plotly
```

### 3) Rodar a aplicação

```powershell
streamlit run app.py
```

Após iniciar, abra a URL exibida no terminal (normalmente `http://localhost:8501`).

## 🧪 Como usar a interface

1. Abra o painel lateral em **🛠️ Painel de Controle**.
2. Selecione um ou mais produtos no filtro **Escolha o Produto**.
3. Analise os indicadores no topo e os dois gráficos principais.
4. Expanda **📂 Ver dados brutos** para inspecionar a tabela filtrada.

## 🗃️ Sobre os dados

Os dados são gerados dinamicamente pela função `carregar_dados()`:
- 200 registros aleatórios
- janela de até 30 dias
- 4 produtos fictícios
- 3 classes de sentimento (`Positivo`, `Neutro`, `Negativo`)
- engajamento entre 100 e 5000
- nota entre 1.0 e 5.0

Por serem aleatórios, os resultados variam a cada execução.

## ⚙️ Personalização rápida

Você pode adaptar facilmente:
- **Produtos**: altere a lista `produtos` em `app.py`
- **Sentimentos**: altere a lista `sentimentos`
- **Volume de dados**: ajuste o `range(200)`
- **Escala de engajamento e nota**: ajuste os limites de `random.randint` e `random.uniform`

## 🛠️ Solução de problemas (Windows)

- Erro de execução de script no PowerShell:
  - rode `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
- `streamlit` não reconhecido:
  - confirme se o ambiente virtual está ativo
  - use `python -m streamlit run app.py`
- Porta ocupada:
  - execute `streamlit run app.py --server.port 8502`

## 📌 Observações

- Projeto com foco educacional e de prototipagem.
- Não há persistência em banco nem ingestão de dados externos.
- Não há suíte de testes automatizados configurada neste repositório.
